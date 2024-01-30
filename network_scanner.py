#! /usr/bin/env python

import scapy.all as scapy
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)#to create arp packet object#pdst is name of field we want to set
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answer_list= scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]#srp allows us to send coustum ether packets. this packet send packet & recieve response.

    print("IP\t\t\tMAC Address\n------------------------------------------")
    for element in answer_list:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)

scan("192.168.130.0/24")

