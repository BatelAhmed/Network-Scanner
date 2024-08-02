#!/usr/bin/env python

import sys
import argparse
from scapy.all import ARP, Ether, srp

def scan(ip):
    print("-------------------------------------------------------")
    print(f"Scanning IP range: {ip}")

    arp_request = ARP(pdst=ip)
    print(f"ARP Request: {arp_request.summary()}")
    print("-------------------------------------------------------")

    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    print(f"Ethernet Frame: {broadcast.summary()}")
    print("-------------------------------------------------------")

    
    arp_request_broadcast = broadcast / arp_request
    print(f"Combined Packet: {arp_request_broadcast.summary()}")
    print("-------------------------------------------------------")

    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    if not answered_list:
        print("No responses received.")
    else: 
        print("-------------------------------------------------------")
        print("Scanning complete. Results:")
        print("-------------------------------------------------------")

    for sent, received in answered_list:
        print(f"IP: {received.psrc}, MAC: {received.hwsrc}")
        print("-------------------------------------------------------")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Network scanner using ARP requests")
    parser.add_argument("-i", "--ip_range", type=str, required=True, help="IP range to scan, e.g., 10.0.0.1/24")
    
    args = parser.parse_args()
    scan(args.ip_range)

