#!/usr/bin/env python

# Find all 'crypto map CRYPTO' entries without AES encryption
# and print entries with configured transform-set

from ciscoconfparse import CiscoConfParse

if __name__ == "__main__":

    config = CiscoConfParse("cisco_ipsec.txt")

    for cryptomap in config.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", 
                                                  childspec=r"set\stransform-set\sAES"):
        print cryptomap.text

        for transform_set in cryptomap.re_search_children(r"set\stransform-set\s"):
        
            print transform_set.text        

