#!/usr/bin/env python
'''
Use Netmiko to enter into configuration mode on pynet-rtr2. Also use
Netmiko to verify your state (i.e. that you are currently in configuration mode).
'''

from netmiko import ConnectHandler
from getpass import getpass
from routers import pynet_rtr2

def main():
    '''
    Use Netmiko to enter into configuration mode on pynet-rtr2. Also use
    Netmiko to verify your state (i.e. that you are currently in configuration mode).
    '''

    ip_address = raw_input("Please enter IP: ")
    password = getpass()

    pynet_rtr2['ip'] = ip_address
    pynet_rtr2['password'] = password

    ssh_conn = ConnectHandler(**pynet_rtr2)

    ssh_conn.config_mode()

    if ssh_conn.check_config_mode():
        print "In config mode"

if __name__ == '__main__':
    main()
