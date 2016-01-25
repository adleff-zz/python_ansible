#!/usr/bin/env python

# load json and yaml files as input and then pretty print to display

import yaml, json
from pprint import pprint

if __name__ == "__main__":


  with open("my_list.yml") as yaml_file:
    yaml_file = yaml.load(yaml_file)

  with open("my_list.json") as json_file:
    json_file = json.load(json_file)



  pprint(yaml_file)
  print "\n" + "\n"
  pprint(json_file)
