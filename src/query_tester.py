import os
import argparse
import pathlib
import logging
import rdflib
from ruamel.yaml import YAML, YAMLError

logging.basicConfig(level=logging.INFO)

def create_sparql(id: str, query: str, input: dict):
  for var_name, values in input.items():
    values = list(map(lambda x: "<"+x+">", values))
    query = query.replace(f"{var_name}",' '.join(values))

  with open(f'sparql/{id}.sparql', 'w') as f:
    f.write(query)
  
  return query

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

  tests['expected_results'] = comp_ques['expected_result']
  tests['endpoints'] = []

  if 'relationgraph' in qm.keys():
    t = {}
    endpoint = qm['relationgraph']
    t['endpoint'] = 'relationship'
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
  print(endpoint)
  g = rdflib.Graph()
  g.parse(endpoint)

  qres = g.query(query)
  results = []
  for row in qres:
    results.append(row.cell)
    
  return results

def compare_results(expected_results: list, results: list):
  return True
  

def run_tests(tests: dict):
  for e in tests['endpoints']:
    endpoint = ""
    print(e)
    if e['endpoint'] == 'relationgraph':
      endpoint = "endpoints/ccf-materialized.owl"
    if e['endpoint'] == 'ccf':
      endpoint = "endpoints/ccf.owl"
    results = run_query(endpoint, e['query'])
    # compare_results(tests['expected_results'], results)

def main(input):
  if input.endswith('yaml') or input.endswith('yml'):
    config_file = os.path.abspath(input)

  tests = parse_tester(config_file)
  run_tests(tests)


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', '--input', type=pathlib.Path, required=True, help="a yaml file")

  args = parser.parse_args()
  main(str(args.input))