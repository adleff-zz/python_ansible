#!/usr/bin/env python
'''
Use Paramiko to retrieve the entire 'show version' output from pynet-rtr2
'''

import time
import paramiko
from getpass import getpass

PYNET_RTR2_PORT = 8022
USERNAME = 'pyclass'

def main():
    '''
    Use Paramiko to retrieve the entire 'show version' output from pynet-rtr2
    '''

    pynet_rtr2_ip = raw_input("Please enter IP: ")
    password = getpass()

    #initialize object for ssh connection
    ssh_conn = paramiko.SSHClient()
    ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_conn.connect(pynet_rtr2_ip, PYNET_RTR2_PORT, USERNAME,
                     password, look_for_keys=False, allow_agent=False)

    remote_shell = ssh_conn.invoke_shell()
    time.sleep(1)

    #send 'terminal length 0' down channel
    output = remote_shell.send('terminal length 0\n')

    # if channel is ready with data, read data
    if remote_shell.recv_ready():
        output = remote_shell.recv(65535)

    remote_shell.send('show version\n')
    time.sleep(1)

    if remote_shell.recv_ready():
        output = remote_shell.recv(65535)

    #print verified result
    print "\n {} \n".format(output)

if __name__ == '__main__':
    main()
