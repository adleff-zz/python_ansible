#!/usr/bin/env python


# create a list full of things, and format the output to yaml and json files

import yaml, json


my_list = range(10)

my_list.append('item1')
my_list.append('item2')
my_list.append({})

my_list[-1]['model']  = 'Cisco 2951 ISR G2'
my_list[-1]['mgmt_ip'] = '10.1.10.1'
my_list[-1]['device_type'] = 'Router' 



with open("my_list.yml", "w") as yaml_file:
    yaml_file.write(yaml.dump(my_list, default_flow_style=False))

with open("my_list.json", "w") as json_file:
    json_file.write(json.dumps(my_list, json_file)) 
