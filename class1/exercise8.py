#!/usr/bin/env python

# find all 'crypto map CRYPTO' entries in cisco_ipsec.txt
# and print along with all child object text

from ciscoconfparse import CiscoConfParse

if __name__ == "__main__":

    config = CiscoConfParse("cisco_ipsec.txt")

    for cryptomap in config.find_objects(r"crypto map CRYPTO"):
    
        print cryptomap.text
        
        for subconfig in cryptomap.children:
            print subconfig.text
