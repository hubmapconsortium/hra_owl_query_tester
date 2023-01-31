import os
import argparse
import pathlib
import logging
import pandas as pd
import glob
from ruamel.yaml import YAML, YAMLError
from runner import Runner

logging.basicConfig(level=logging.INFO)

def create_sparql(id: str, query: str, input: dict):
  for var_name, values in input.items():
    values = list(map(lambda x: "<"+x+">", values))
    query = query.replace(f"{var_name}",' '.join(values))
  output = f'sparql/{id}.sparql'
  
  with open(output, 'w') as f:
    f.write(query)
  
  return output

def parse_tester(config) -> dict:
  tests = {}
  ryaml = YAML(typ='safe')
  with open(config, "r") as f:
    try:
      comp_ques = ryaml.load(f)
    except YAMLError as exc:
      logging.info(f'Failed to load test config: {config}')

  input = comp_ques['input']
  qm = comp_ques['query_mechanism']

  tests['description'] = comp_ques['description']
  tests['expected_results'] = comp_ques['expected_result']
  tests['endpoints'] = []

  if 'relationgraph' in qm.keys():
    t = {}
    endpoint = qm['relationgraph']
    t['endpoint'] = 'relationgraph'
    t['query'] = create_sparql(f"mat-{comp_ques['id']}", endpoint['query'], input)
    tests['endpoints'].append(t)
  if 'ccf' in qm.keys():
    t = {}
    endpoint = qm['ccf']
    t['endpoint'] = 'ccf'
    t['query'] = create_sparql(f"ccf-{comp_ques['id']}", endpoint['query'], input)
    tests['endpoints'].append(t)

  return tests

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

def is_test_passed(expected_results, results):
  if os.path.getsize(results) == 0:
    logging.info("No results found. Please, check the query.")
    return False
   
  missing, misplaced = compare_results(expected_results=expected_results, results=results)
  if len(missing) == 0 and len(misplaced) == 0:
    return True
  if len(missing) or len(misplaced):
    if len(missing):
      logging.info(f"Following terms are missing: {missing}")
    if len(misplaced):
      logging.info(f"Following terms are not expected: {misplaced}")
    return False


def run_tests(tests: dict):
  for e in tests['endpoints']:
    results = run_query(e['endpoint'], e['query'])
    if is_test_passed(expected_results=tests['expected_results'], results=results):
      logging.info(f"PASSED for {e['endpoint']}")
    else:
      logging.info(f"FAILED for {e['endpoint']}")

def main(input):
  if os.path.isdir(input):
    if not input.endswith(os.path.sep):
      input += os.path.sep
    test_docs = glob.glob(input + "*.yaml")
    test_docs.extend(glob.glob(input + "*.yml"))
  elif input.endswith('.yaml') or input.endswith('.yml'):
    test_docs = [os.path.abspath(input)]
  else:
    logging.error("Given path has unsupported file extension.", )

  for test_doc in test_docs:
    logging.info(f'Testing {test_doc}')
    config_file = os.path.abspath(test_doc)
    tests = parse_tester(config_file)
    logging.info(f"Description: {tests['description']}")                                                                               
    run_tests(tests)


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', '--input', type=pathlib.Path, required=True, help="a yaml file")

  args = parser.parse_args()
  main(str(args.input))