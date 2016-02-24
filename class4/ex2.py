#!/usr/bin/env python
'''
Use Paramiko to change the 'logging buffered <size>' configuration on pynet-rtr2. This will require that you enter into configuration mode.
'''

import re
import time
import paramiko
from getpass import getpass

PYNET_RTR2_PORT = 8022
USERNAME = 'pyclass'

def main():

    pynet_rtr2_ip = raw_input("Please enter IP address: ")
    password = getpass()

    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_conn_pre.connect(pynet_rtr2_ip, PYNET_RTR2_PORT, USERNAME,
                            password, look_for_keys=False, allow_agent=False)

    remote_conn = remote_conn_pre.invoke_shell()
    time.sleep(1)

    remote_conn.send('terminal length 0\n')
    time.sleep(1)
    remote_conn.send('config t\n')
    time.sleep(1)
 
    if remote_conn.recv_ready():
        output = remote_conn.recv(65535)

    if re.search(r'\(config\)#$', output):
        remote_conn.send('logging buffered 999999\n')  
        time.sleep(1)
        remote_conn.send('do show run | in logging\n')
        time.sleep(1)
        
    if remote_conn.recv_ready():
        output = remote_conn.recv(65535)
        print output
    
if __name__ == '__main__':
    main()
