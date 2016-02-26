#!/usr/bin/env python
'''
Use Netmiko to change the logging buffer size (logging buffered <size>) on pynet-rtr2
'''

from netmiko import ConnectHandler
from getpass import getpass
from routers import pynet_rtr2

def main():
    '''
    Use Netmiko to change the logging buffer size (logging buffered <size>) on pynet-rtr2
    '''

    ip_address = raw_input("Enter IP address: ")
    password = getpass()

    pynet_rtr2['ip'] = ip_address
    pynet_rtr2['password'] = password

    ssh_conn = ConnectHandler(**pynet_rtr2)

    ssh_conn.config_mode()

    if ssh_conn.check_config_mode:
        ssh_conn.send_command('logging buffered 999999')
        ssh_conn.exit_config_mode()

    output = ssh_conn.send_command('show run | in logging')
    print output

if __name__ == '__main__':
    main()
