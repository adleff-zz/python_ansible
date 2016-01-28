#!/usr/bin/env python

# provides functions for telnetting to routers,
# sending commands and printing command output 

import sys
import telnetlib
import time

class TelnetRouter(object):

    def __init__(self, ip_addr, telnet_port=23, telnet_timeout=5):

        self.ip_addr = ip_addr
        self.telnet_port = telnet_port
        self.telnet_timeout = telnet_timeout

        try:
            self.remote_conn = telnetlib.Telnet(self.ip_addr, self.telnet_port, self.telnet_timeout)
        except:
            sys.exit("Connection Timeout")

    def tr_open(self, username, password):
         
        output = self.remote_conn.read_until("sername:", self.telnet_timeout)
        self.remote_conn.write(username + "\n")
        output += self.remote_conn.read_until("ssword:", self.telnet_timeout)
        self.remote_conn.write(password + "\n")
 
        time.sleep(1)
        output += self.remote_conn.read_very_eager()

        return output 

    def tr_cmd(self, cmd):

        self.remote_conn.write(cmd + "\n")

        time.sleep(1)
        output = self.remote_conn.read_very_eager() 

        return output


    def tr_close(self):
        self.remote_conn.close()


def main():

    test = TelnetRouter("50.76.53.27")

    output = test.tr_open("pyclass", "88newclass")
    output += test.tr_cmd("terminal length 0")
    output += test.tr_cmd("show ip int brief")

    print output
    test.tr_close()


if __name__ == "__main__":
    main()
