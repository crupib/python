import os
import sys
import argparse
import json
import simplejson as json


class ExampleInventory(object):

    def __init__(self):
        self.inventory = {}
        self.read_cli_args()
        self.inventory = self.example_inventory()
        print(json.dumps(self.inventory))

# Example inventory for testing.

    def example_inventory(self):
        host_ip_dict={"ansible_1": "192.168.99.210"}
        print(host_ip_dict.keys())
        print(host_ip_dict.values())
        return {'bcgroup': {'hosts': ['192.168.28.71', '192.168.28.72', host_ip_dict.values()],
                'vars': {'ansible_ssh_user': 'vagrant',
                'example_variable': 'value'}},
                '_meta': {'hostvars': { host_ip_dict.values(): {'host_specific_var': host_ip_dict.keys()},  '192.168.28.71': {'host_specific_var': 'foo'},
                '192.168.28.72': {'host_specific_var': 'bar'}}}}

# Empty inventory for testing.

    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}

# Read the command line args passed to the script.

    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action='store_true')
        parser.add_argument('--host', action='store')
        self.args = parser.parse_args()


# Get the inventory.

ExampleInventory()
