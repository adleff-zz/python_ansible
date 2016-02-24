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
    
    pynet_rtr2_ip = raw_input("Please enter IP: ")
    password = getpass()
    
    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_conn_pre.connect(pynet_rtr2_ip, PYNET_RTR2_PORT, USERNAME,
                            password, look_for_keys=False, allow_agent=False)

    remote_conn = remote_conn_pre.invoke_shell()
    time.sleep(1)

    output = remote_conn.send('terminal length 0\n')
    
    if remote_conn.recv_ready():
        output = remote_conn.recv(65535)

    remote_conn.send('show version\n')      
    time.sleep(1)

    if remote_conn.recv_ready():
        output = remote_conn.recv(65535)

    print "\n {} \n".format(output) 

if __name__ == '__main__':
    main()


