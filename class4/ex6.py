#!/usr/bin/env python
'''
Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx.
'''

from netmiko import ConnectHandler
from getpass import getpass
from routers import pynet_rtr1, pynet_rtr2, pynet_jnpr_srx1

def main():
    '''
    Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx.
    '''

    ip_address = raw_input("Please enter IP: ")
    password = getpass()
 
    pynet_rtr1['ip'] = ip_address
    pynet_rtr2['ip'] = ip_address
    pynet_jnpr_srx1['ip'] = ip_address

    pynet_rtr1['password'] = password
    pynet_rtr2['password'] = password
    pynet_jnpr_srx1['password'] = password

    #for each router send show arp command and print result
    for router in (pynet_rtr1, pynet_rtr2, pynet_jnpr_srx1):
        ssh_conn = ConnectHandler(verbose=False, **router)
        output = ssh_conn.send_command('show arp')

        print ">>> {}: \n".format(ssh_conn.ip)
        print output
        print ">>>\n"

if __name__ == '__main__':
    main()
