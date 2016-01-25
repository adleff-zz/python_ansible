#!/usr/bin/env python

# Find all 'crypto map CRYPTO' entries without AES encryption
# and print entries with configured transform-set

import re
from ciscoconfparse import CiscoConfParse


config = CiscoConfParse("cisco_ipsec.txt")

cryptomap = config.find_objects_wo_child(parentspec=r"crypto map CRYPTO", 
                                         childspec=r"set transform-set AES")
    
for object in cryptomap:
    for i in object.children:
        if 'set transform-set' in i.text:       
            transform_set = re.search(r"set transform-set (.*)$", i.text)
            transform_name = transform_set.group(1)
    
    print "%s:  %s\n" % (object.text, transform_name)


