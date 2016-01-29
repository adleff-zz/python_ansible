#!/usr/bin/env python
'''
Create a script that connects to both routers (pynet-rtr1 and pynet-rtr2) and prints out both the MIB2 sysName and sysDescr.
'''

import snmp_helper

IP = '50.76.53.27'
COMMUNITY = 'galileo'
SYSNAME_OID = '1.3.6.1.2.1.1.5.0'
SYSDESCR_OID = '1.3.6.1.2.1.1.1.0'

def main():

    rtr1 = (IP, COMMUNITY, 7961)
    rtr2 = (IP, COMMUNITY, 8061)

    rtr1_sysname = snmp_helper.snmp_get_oid(rtr1, SYSNAME_OID)
    rtr1_sysdescr = snmp_helper.snmp_get_oid(rtr1, SYSDESCR_OID)

    rtr2_sysname = snmp_helper.snmp_get_oid(rtr2, SYSNAME_OID)
    rtr2_sysdescr = snmp_helper.snmp_get_oid(rtr2, SYSDESCR_OID)

    print "rtr1 sysname: %s\n" % snmp_helper.snmp_extract(rtr1_sysname)
    print "rtr1 sysdescr: %s\n" % snmp_helper.snmp_extract(rtr1_sysdescr)

    print "rtr2 sysname: %s\n" % snmp_helper.snmp_extract(rtr2_sysname)
    print "rtr2 sysdescr: %s\n" % snmp_helper.snmp_extract(rtr2_sysdescr)

if __name__ == "__main__":
    main()
