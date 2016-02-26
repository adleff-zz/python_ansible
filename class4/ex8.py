#!/usr/bin/env python
'''
Use Netmiko to change the logging buffer size (logging buffered <size>)
and to disable console logging (no logging console) from a file on
both pynet-rtr1 and pynet-rtr2
'''

from netmiko import ConnectHandler
from getpass import getpass
from routers import pynet_rtr1, pynet_rtr2

def main():
    '''
    Use Netmiko to change the logging buffer size (logging buffered <size>)
    and to disable console logging (no logging console) from a file on
    both pynet-rtr1 and pynet-rtr2
    '''

    ip_address = raw_input("Please enter IP address: ")
    password = getpass()

    pynet_rtr1['ip'] = ip_address
    pynet_rtr2['ip'] = ip_address
    pynet_rtr1['password'] = password
    pynet_rtr2['password'] = password

    #for each router load config from
    #file and print result

    for router in (pynet_rtr1, pynet_rtr2):
        ssh_conn = ConnectHandler(verbose=False, **router)
        ssh_conn.send_config_from_file('ex8_config.txt')

        output = ssh_conn.send_command('show run | in logging')

        print "\n>>> {}:{}  \n".format(ssh_conn.ip, ssh_conn.port)
        print output
        print ">>>\n"

if __name__ == '__main__':
    main()
