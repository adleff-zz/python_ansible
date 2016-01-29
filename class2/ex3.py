#!/usr/bin/env python
'''
Write a script that connects to the lab pynet-rtr1, logins, and executes the
'show ip int brief' command.
'''

import telnetlib
import time
import socket
import sys
import getpass

TELNET_PORT = 23
TELNET_TIMEOUT = 6


class TelnetRouter(object):

    def __init__(self, ip_addr, username, password):
        '''
        Grab input and initialize objects
        '''
        self.ip_addr = ip_addr
        self.username = username
        self.password = password
    


    def send_command(self, remote_conn, cmd):
        '''
        Send a command down the telnet channel

        Return the response
        '''
        cmd = cmd.rstrip()
        remote_conn.write(cmd + '\n')
        time.sleep(1)
        return remote_conn.read_very_eager()

    def login(self, remote_conn, username, password):
        '''
        Login to network device
        '''
        output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
        remote_conn.write(username + '\n')
        output += remote_conn.read_until("ssword:", TELNET_TIMEOUT)
        remote_conn.write(password + '\n')
        return output

    def disable_paging(self, remote_conn, paging_cmd='terminal length 0'):
        '''
        Disable the paging of output (i.e. --More--)
        '''
        return self.send_command(remote_conn, paging_cmd)

    def telnet_connect(self, ip_addr):
        '''
        Establish telnet connection
        '''
        try:
            return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
        except socket.timeout:
            sys.exit("Connection timed-out")

 

def main():
    '''
    Write a script that connects to the lab pynet-rtr1, logins, and executes the
    'show ip int brief' command.
    '''

    device = TelnetRouter(raw_input('IP Address: '), raw_input('Username: '), getpass.getpass()) 

    remote_conn = device.telnet_connect(device.ip_addr)

    output = device.login(remote_conn, device.username, device.password)

    time.sleep(1)
    remote_conn.read_very_eager()
    device.disable_paging(remote_conn)


    output = device.send_command(remote_conn, 'show ip int brief')
    
    print "\n\n"
    print output
    print "\n\n"

    remote_conn.close()

if __name__ == "__main__":
    main()
