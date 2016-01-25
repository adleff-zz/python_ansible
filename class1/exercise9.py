#!/usr/bin/env python

# find all 'crypto map CRYPTO' entries in cisco_ipsec.txt
# that are using PFS group 2 and print all matches along 
# with all child object

from ciscoconfparse import CiscoConfParse


config = CiscoConfParse("cisco_ipsec.txt")

for cryptomap in config.find_objects_w_child(parentspec="crypto map CRYPTO",
                                             childspec="set pfs group2"):
    print cryptomap.text

    for subconfig in cryptomap.children:
        print subconfig.text
