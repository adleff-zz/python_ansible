#!/usr/bin/env python
'''
Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2.
'''

import pexpect
from getpass import getpass

USERNAME = 'pyclass'
PYNET_RTR2_PORT = 8022

def main():
    '''
    Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2.
    '''

    pynet_rtr2_ip = raw_input("Please enter IP address: ")
    password = getpass()

    ssh_conn = pexpect.spawn('ssh -l {} {} -oStrictHostKeyChecking=no -p {}'.format(USERNAME,
                                                             pynet_rtr2_ip, PYNET_RTR2_PORT))

    ssh_conn.timeout = 3
    ssh_conn.expect('ssword:')

    ssh_conn.sendline(password)
    ssh_conn.expect('pynet-rtr2#')

    ssh_conn.sendline('show ip int brief')
    ssh_conn.expect('pynet-rtr2#')

    print ssh_conn.before

if __name__ == '__main__':
    main()
