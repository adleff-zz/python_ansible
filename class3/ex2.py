#!/usr/bin/env python
'''
Using SNMPv3 create two SVG image files.  

The first image file should graph the input and output octets on interface FA4 on pynet-rtr1 every five minutes for an hour.  
Use the pygal library to create the SVG graph file. Note, you should be doing a subtraction here 
(i.e. the input/output octets transmitted during this five minute interval).  

The second SVG graph file should be the same as the first except graph the unicast packets received and transmitted.

The relevant OIDs are as follows:

('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5')
('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5')
('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5')
('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5'),
('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5')
'''

import time
import pygal
from snmp_helper import snmp_extract, snmp_get_oid_v3
from getpass import getpass

ip_address = raw_input("Please enter IP address: ")
snmp_key  = getpass(prompt="Please enter SNMPv3 key: ")
pynet_rtr1 = (ip_address, '7961')
snmp_user = ('pysnmp', snmp_key, snmp_key)

# defined interface OIDs 

interface_oids = ( 
('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5'),
('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5'),
('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5'),
('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5')
)


# initialize lists to store polled interface counters
fa4_input_octets = []
fa4_output_octets = []
fa4_input_packets = []
fa4_output_packets = []

# initialize lists to track interface base counters
fa4_input_octets_base = [] 
fa4_output_octets_base = [] 
fa4_input_packets_base = []
fa4_output_packets_base = []

'''
Every 5 minutes, polls each interface OID and subtract the 
base value from the current polled value.  The interface counters
increment beginning at interface uptime so we need subtraction here
in order to reflect the accurate values.
'''

for interval in range(0, 65, 5):
    
    for interface_counter,oid in interface_oids:
        print ">>>> Polling interface counter {0} on {1}, {2} minute interval.\n\n\n".format(
              interface_counter, pynet_rtr1[0], interval)

        if interface_counter is 'ifInOctets_fa4':
            current_counter = (snmp_extract
            (snmp_get_oid_v3(pynet_rtr1, snmp_user, oid)))
            
            if fa4_input_octets_base:
                fa4_input_octets.append(int(current_counter) - int(fa4_input_octets_base[-1]))

            fa4_input_octets_base.append(current_counter)
                   
        if interface_counter is 'ifOutOctets_fa4':
            current_counter = (snmp_extract
            (snmp_get_oid_v3(pynet_rtr1, snmp_user, oid)))


            if fa4_output_octets_base:
                fa4_output_octets.append(int(current_counter) - int(fa4_output_octets_base[-1]))

            fa4_output_octets_base.append(current_counter)
        
        if interface_counter is 'ifInUcastPkts_fa4':
            current_counter = (snmp_extract
            (snmp_get_oid_v3(pynet_rtr1, snmp_user, oid)))
      

            if fa4_input_packets_base:
                fa4_input_packets.append(int(current_counter) - int(fa4_input_packets_base[-1]))

            fa4_input_packets_base.append(current_counter)

        if interface_counter is 'ifOutUcastPkts_fa4':
            current_counter = (snmp_extract
            (snmp_get_oid_v3(pynet_rtr1, snmp_user, oid)))
      

            if fa4_output_packets_base:
                fa4_output_packets.append(int(current_counter) - int(fa4_output_packets_base[-1]))

            fa4_output_packets_base.append(current_counter) 

    #Test if we are still running intervals, if so wait 5 minutes for next cycle
    if interval < 60:        
        time.sleep(300)

# draw two line graphs, one containing I/O Octets and the other containing I/O Packets

line_chart_octets = pygal.Line()
line_chart_octets.title = 'pynet-rtr1 Input/Output octets in 5 minute increments'
line_chart_octets.x_labels = map(str, range(5, 65, 5))
line_chart_octets.add('InputOctets', fa4_input_octets)
line_chart_octets.add('OutputOctets', fa4_output_octets)
line_chart_octets.render_to_file('inout_octets.svg')

line_chart_packets = pygal.Line()
line_chart_packets.title = 'pynet-rtr1 Input/Output packets in 5 minute increments'
line_chart_packets.x_labels = map(str, range(5, 65, 5))
line_chart_packets.add('InputPackets', fa4_input_packets)
line_chart_packets.add('OutputPackets', fa4_output_packets)
line_chart_packets.render_to_file('inout_packets.svg')





'''
print fa4_input_octets
print fa4_output_octets
print fa4_input_octets_base[-1]
print fa4_output_octets_base[-1]
'''
