import os
import argparse
import pathlib
import logging
import pandas as pd
import glob
from ruamel.yaml import YAML, YAMLError
from runner import Runner
from mdutils import MdUtils

logging.basicConfig(level=logging.INFO)

TERM_LABEL_QUERY = '''
  PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

  SELECT ?term ?label
  WHERE {
    VALUES ?term {
      terms
    }
    ?term rdfs:label ?label .
  }
'''

def create_sparql(id: str, query: str, input: dict):
  for var_name, values in input.items():
    values = list(map(lambda x: "<"+x+">", values))
    query = query.replace(f"{var_name}",' '.join(values))
  output = f'sparql/{id}.sparql'
  
  with open(output, 'w') as f:
    f.write(query)
  
  return output

def parse_tester(config) -> dict:
  ryaml = YAML(typ='safe')
  with open(config, "r") as f:
    try:
      comp_ques = ryaml.load(f)
    except YAMLError as exc:
      logging.info(f'Failed to load test config: {config}')

  return comp_ques

def get_labels(terms):
  input = {'terms': terms}
  results_file = run_query('hra', create_sparql('labels', TERM_LABEL_QUERY, input))
  return pd.read_csv(results_file)

def run_query(endpoint, query):
  runner = Runner()
  
  results = runner.run_cmd(endpoint=endpoint, query_file=query)
  
  return results

def compare_results(expected_results: dict, results: pathlib.Path):
  var = list(expected_results.keys())[0]
  res = set(pd.read_csv(results)[f'{var}'])
  exp = set(expected_results[f'{var}'])
  missing = exp - res
  misplaced = res - exp
  
  return missing, misplaced

def is_test_passed(expected_results, results, report):
  if os.path.getsize(results) == 0:
    logging.info("No results found. Please, check the query.")
    return False
   
  missing, misplaced = compare_results(expected_results=expected_results, results=results)
  if len(missing) == 0 and len(misplaced) == 0:
    return True
  if len(missing) or len(misplaced):
    if len(missing):
      report.new_paragraph(text="Following terms are missing:")
      labels = get_labels(list(missing))
      
      for _, row in labels.iterrows():
        report.new_paragraph(text=f"[{row['label']}]({row['term']})")
      logging.info(f"Following terms are missing: {missing}")
      
    if len(misplaced):
      report.new_paragraph(text="Following terms are not expected:")
      labels = get_labels(list(misplaced))
      
      for _, row in labels.iterrows():
        report.new_paragraph(text=f"[{row['label']}]({row['term']})")
      logging.info(f"Following terms are not expected: {misplaced}")
    return False

def run_tests(tests: dict, report: MdUtils):
  endpoints = tests["query_mechanism"].keys()
  for test in tests['tests']:
    for e in endpoints:
      query = tests['query_mechanism'][e]['query']
      results = run_query(e, create_sparql(tests['id'], query, test['input']))
      report.new_paragraph(text=test['test'], bold_italics_code="bi")
      report.new_paragraph(text="Input terms", bold_italics_code="b")
      for input, value in test['input'].items():
        report.new_paragraph(text=f"{input}")
        labels = get_labels(value)
        for _, row in labels.iterrows():
          report.new_paragraph(text=f"[{row['label']}]({row['term']})")
      if is_test_passed(expected_results=test['expected_result'], results=results, report=report):
        report.new_paragraph(text=f"PASSED using {e}", bold_italics_code="b")
        logging.info(f"PASSED for {e}")
      else:
        report.new_paragraph(text=f"FAILED using {e}", bold_italics_code="b")
        logging.info(f"FAILED for {e}")
  
  return report

def main(input):
  if os.path.isdir(input):
    if not input.endswith(os.path.sep):
      input += os.path.sep
    test_docs = glob.glob(input + "*.yaml")
    test_docs.extend(glob.glob(input + "*.yml"))
  elif input.endswith('.yaml') or input.endswith('.yml'):
    test_docs = [os.path.abspath(input)]
  else:
    logging.error("Given path has unsupported file extension.")
    return False

  test_results = MdUtils(file_name='results/README.md', title='Competency Questions Results')
  logging.info("Look into the file at 'results/README.md' to have a user friendly view of the reports.")
  for test_doc in test_docs:
    test_results.new_header(1, f"Test results for {test_doc}")
    logging.info(f'Testing {test_doc}')
    config_file = os.path.abspath(test_doc)
    tests = parse_tester(config_file)
    test_results.new_paragraph(text=f"{tests['description']}")
    test_results = run_tests(tests, test_results)
    
  test_results.create_md_file()


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', '--input', type=pathlib.Path, required=True, help="a yaml file")

  args = parser.parse_args()
  main(str(args.input))
