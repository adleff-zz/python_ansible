#!/usr/bin/env python
'''
Use my newly defined tr.py module to pull 
'show ip int brief' output from pynet-rtr1
'''

import tr
import getpass

def main():
    '''
    Setup instance of TelnetRouter and send 'show ip int brief'
    '''

    router = tr.TelnetRouter(raw_input("IP Address: "), raw_input("Username: "), getpass.getpass())

    output = router.tr_cmd("terminal length 0")

    output = router.tr_cmd("show ip int brief")

    print output

    router.tr_close()


if __name__ == "__main__":
    main()

    
