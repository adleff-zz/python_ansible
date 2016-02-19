#!/usr/bin/env python
'''
Provides functions to assist with detecting configuration
changes running-configuration on Cisco machines
'''

import pickle
import os.path
from email_helper import send_mail

class NewMachine(object):
    '''
    Create a object used to store machine OID data
    '''
    def __init__(self, machine_name, machine_last_change):
        '''
        Initialize a new machine object and store machine name,
        the current uptime value and last change value
        '''

        self.machine_name = machine_name
        self.machine_last_change = machine_last_change


def email_alert(alert_obj):
    '''
    E-mail alert message that running_config has changed
    Include uptime seconds that config change occurred
    '''

    recipient = 'adamleff@gmail.com'
    subject = '{0}: Running_config has changed'.format(alert_obj.machine_name)
    message = '''
    
    Machine: {0} running-config changed at uptime: {1}

    '''.format(alert_obj.machine_name, int(alert_obj.machine_last_change) / 100)

    sender = 'aleff@twb-tech.com'
    send_mail(recipient, subject, message, sender)


def load_stored_machines(pickle_file):
    '''
    Find any currently stored Machine objects from file and return
    as a dictionary object
    '''

    # If no stored machines found return empty dict

    if not os.path.isfile(pickle_file):
        print "\nMachine file does not exist.  Returning empty dictionary.\n"

        return {}

    # Create dictionary for found stored machines

    stored_machines = {} 

    with open(pickle_file, 'r') as file:
        while True:
            try:
                found_machines = pickle.load(file)
                stored_machines[found_machines.machine_name] = found_machines
            except EOFError:
                return stored_machines 
