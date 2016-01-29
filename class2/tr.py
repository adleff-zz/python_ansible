#!/usr/bin/env python
'''
provides functions for telnetting to routers,
sending commands and printing command output 
'''

import sys
import telnetlib
import time
import socket
import getpass

TELNET_PORT = 23
TELNET_TIMEOUT = 5

class TelnetRouter(object):
    '''
    Store attributes and methods used to telnet to remote devices,
    send commands and read output
    '''

    def __init__(self, ip_addr, username, password):
        '''
        Initiate object
        '''

        self.ip_addr = ip_addr
        self.username = username
        self.password = password
        
        try:
            self.remote_conn = telnetlib.Telnet(self.ip_addr, TELNET_PORT, TELNET_TIMEOUT)
        except socket.timeout:
            sys.exit("Connection Timeout")


        output = self.remote_conn.read_until("sername:", TELNET_TIMEOUT)
        self.remote_conn.write(self.username + "\n")
        output = self.remote_conn.read_until("ssword:", TELNET_TIMEOUT)
        self.remote_conn.write(self.password + "\n")
 
        time.sleep(1)
        output = self.remote_conn.read_very_eager()


    def tr_cmd(self, cmd):
        '''
        Send input command to remote device
        '''

        self.remote_conn.write(cmd + "\n")

        time.sleep(1)
        output = self.remote_conn.read_very_eager()
        output = output.lstrip(cmd)
        output = output.lstrip()

        return output


    def tr_close(self):
        '''
        close connection to remote device
        '''

        self.remote_conn.close()


def main():
    ''' 
    Call TelnetRouter object and collect output
    of 'show ip int brief'
    '''

    test = TelnetRouter(raw_input("IP Address: "), raw_input("Username: "), getpass.getpass())

    test.tr_cmd("terminal length 0")
    output = test.tr_cmd("show ip int brief")

    print output
    test.tr_close()


if __name__ == "__main__":
    main()
