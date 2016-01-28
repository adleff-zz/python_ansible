#!/usr/bin/env python

# Use my newly defined TelnetRouter module to pull \
# 'show ip int brief' from pynet-rtr1

from telnetrouter import TelnetRouter

def main():

    remote_conn = TelnetRouter("50.76.53.27")

    output = remote_conn.tr_open("pyclass", "88newclass")

    output += remote_conn.tr_cmd("terminal length 0")

    output += remote_conn.tr_cmd("show ip int brief")

    print output

    remote_conn.tr_close()


if __name__ == "__main__":
    main()

    
