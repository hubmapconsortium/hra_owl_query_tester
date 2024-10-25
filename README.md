# ccf_owl_query_tester
A framework for specifying and testing queries against HRA.owl based on competency questions.

## Motivation:

Ad hoc testing of the HRA ontology has uncovered cases where simple use-case queries do not work.  This repo aims to run these test more systematically.

## Aim:

A YAML configuration will specify:

* A competency question (expressed in plain text).  
* A list of objects specifying
   * Input term(s)
   * A minimal answer - some set of terms that the  query should return, based on the intention of ASCT+B table author.
* A list of objects specifying:
  * An endpoint
  * A formal query in the correct syntax for the endpoint

Make a JSON schema + add validator for YAML.
  
A Python runner + GitHub actions will run these queries against the endpoints, reporting success, or not.

### Some simple test queries:
* All cells in loc X all cells of type Y
* All cells expressing marker Z (more strictly, for which Z is recorded as a marker)
* All cells in loc X of type Y expressing marker Z
* Location(s) of cell type X
* Location(s) of cell type X expressing marker Z
 
### Potential endpoints/query mechanisms:
* HRA.owl + relationgraph --> SPARQL queries of precomputed OWL inferences.  Pre-generate file with RG. SPARQL Queries could be run in ROBOT.
* HRA.owl --> SPARQL queries of HRA properties (Use file as-is Queries in ROBOT)
* HRA.owl + EL queries via [OWLERY](https://github.com/phenoscape/owlery) (would require firing up local server - needs containerization)

## How to add tests and run them

1. Create a yaml file with the test and save it in the tests folder
1. After the test is pushed to the main branch, the GitHub Action runs all tests. The result of each test is in the file `results/test_log.txt`.
