#!/usr/bin/env python
'''
Use PExpect to change the logging buffer size (logging buffered <size>) on pynet-rtr2. Verify this change by examining the output of 'show run'.
'''

import pexpect
from getpass import getpass

USERNAME = 'pyclass'
PYNET_RTR2_PORT = 8022


def main():

    pynet_rtr2_ip = raw_input("Please enter IP address: ")
    password = getpass()

    ssh_conn = pexpect.spawn('ssh -l {} {} -oStrictHostKeyChecking=no -p {}'.format(USERNAME, 
                                                             pynet_rtr2_ip, PYNET_RTR2_PORT))

    ssh_conn.timeout = 3
    ssh_conn.expect('ssword:')

    ssh_conn.sendline(password)
    ssh_conn.expect('pynet-rtr2#')

    ssh_conn.sendline('config t')
    ssh_conn.expect(r'pynet-rtr2\(config\)#')

    ssh_conn.sendline('logging buffered 999999')
    ssh_conn.expect(r'pynet-rtr2\(config\)#')

    ssh_conn.sendline('do show run | in logging')
    ssh_conn.expect(r'pynet-rtr2\(config\)#')

    print ssh_conn.before 
    
if __name__ == '__main__':
    main()
