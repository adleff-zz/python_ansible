#!/usr/bin/env python

import pickle
from getpass import getpass
from snmp_helper import snmp_extract, snmp_get_oid_v3
from config_check import load_stored_machines, email_alert, NewMachine

def main():
    '''
    Using SNMPv3 create a script that detects router configuration changes.
    If the running configuration has changed, then email an alert message
    identifying the router that changed and the time that it changed.
    '''

    NAME_OID = '1.3.6.1.2.1.1.5.0'
    CHANGE_OID = '1.3.6.1.4.1.9.9.43.1.1.1.0'

    pickle_file = 'machine_file.pkl'

    ip_address = raw_input("Enter IP address: ") 
    machines = ((ip_address, '7961'), (ip_address, '8061'))
    username = raw_input("Enter SNMPv3 Username: ")
    authentication_key = getpass(prompt="Enter Authentication key: ")
    encryption_key = getpass(prompt="Enter Encryption key: ")

    snmp_user = (username, authentication_key, encryption_key)

    # load stored machines from pickle_file into dictionary object

    stored_machines = load_stored_machines(pickle_file)

    # create list to store machine objects created from config_check.NewMachine 

    pickle_dump_list = []


    # using SNMPv3 poll all defined machines, 
    # grab sysName and ccmHistoryRunningLastChanged OIDs

    for values in machines:
        snmp_data = []

        for snmp_oid in (NAME_OID, CHANGE_OID):
            snmp_poll = snmp_extract(snmp_get_oid_v3(values, snmp_user, snmp_oid))
            snmp_data.append(snmp_poll)

        machine_name = snmp_data[0]
        machine_last_change = snmp_data[1]

        pickle_dump_list.append(NewMachine(machine_name, machine_last_change))


        # test if polled sysName matches a previously stored device,
        # if match and config change is detected send email alert

        if machine_name in stored_machines:
            alert_obj = stored_machines[machine_name]

            if machine_last_change > alert_obj.machine_last_change:
                print "\n{0}: running-config has changed!".format(machine_name)
                email_alert(alert_obj)

            else:
                print "\n{0}: No running-config change detected!".format(machine_name)

        else:
            print "{0}: Not previously found. Saving to {1}".format(machine_name, pickle_file)
            
    

    with open(pickle_file, 'w') as file:
        for list_item in pickle_dump_list:
            pickle.dump(list_item, file)

if __name__ == '__main__':
    main()
