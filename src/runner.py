import pathlib
import subprocess
import logging
import os.path

class Runner():
  def __init__(self) -> None:
      pass
  
  def run_cmd(self, input_file: pathlib.Path, query_file: pathlib.Path):
      file_name = os.path.splitext(os.path.basename(query_file))[0]

      CMD = f"robot query --input {input_file} --query {query_file} results/{file_name}.csv"
      p = subprocess.Popen([CMD], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True)
      (_, err) = p.communicate()
      if err:
          logging.error(err)
      if p.returncode != 0:
          raise Exception(f'Failed: {CMD}')
      
      return f'results/{file_name}.csv'