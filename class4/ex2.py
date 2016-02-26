#!/usr/bin/env python
'''
Use Paramiko to change the 'logging buffered <size>' configuration on pynet-rtr2.
This will require that you enter into configuration mode.
'''
import re
import time
import paramiko
from getpass import getpass

PYNET_RTR2_PORT = 8022
USERNAME = 'pyclass'

def main():
    '''
    Use Paramiko to change the 'logging buffered <size>' configuration on pynet-rtr2.
    This will require that you enter into configuration mode.
    '''
    pynet_rtr2_ip = raw_input("Please enter IP address: ")
    password = getpass()

    #initialize object for ssh connection
    ssh_conn = paramiko.SSHClient()
    ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_conn.connect(pynet_rtr2_ip, PYNET_RTR2_PORT, USERNAME,
                     password, look_for_keys=False, allow_agent=False)

    remote_shell = ssh_conn.invoke_shell()
    time.sleep(1)

    #send 'terminal length 0' down channel
    remote_shell.send('terminal length 0\n')
    time.sleep(1)
    remote_shell.send('config t\n')
    time.sleep(1)

    if remote_shell.recv_ready():
        output = remote_shell.recv(65535)

    #test that we are in config mode
    if re.search(r'\(config\)#$', output):
        remote_shell.send('logging buffered 999999\n')
        time.sleep(1)
        remote_shell.send('do show run | in logging\n')
        time.sleep(1)

    #print verified results
    if remote_shell.recv_ready():
        output = remote_shell.recv(65535)
        print output

if __name__ == '__main__':
    main()
