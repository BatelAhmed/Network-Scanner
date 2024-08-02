# Network Scanner

## Overview

This is a simple Python-based network scanner that utilizes ARP requests to identify active devices on a local network. The script is designed to scan a specified IP range and return the IP and MAC addresses of devices that respond.

## Requirements

- Python 3.x
- Scapy library

### Installation

To install the required dependencies, use the following command:

```bash
pip install scapy

Usage

To use the network scanner, run the following command in your terminal:

bash

python network_scanner.py -i <IP_RANGE>

Example

bash

python network_scanner.py -i 192.168.1.0/24

This will scan the IP range 192.168.1.0/24 and display the IP and MAC addresses of devices that are active on the network.
Script Details

    scan(ip): The core function that sends ARP requests over the specified IP range and captures responses. It then prints the IP and MAC addresses of all responding devices.

    argparse: Used to handle command-line arguments. The -i or --ip_range argument is mandatory and specifies the IP range to scan.

Example Output

markdown

-------------------------------------------------------
Scanning IP range: 192.168.1.0/24
-------------------------------------------------------
ARP Request: ARP who-has 192.168.1.0/24 says 0.0.0.0
-------------------------------------------------------
Ethernet Frame: Ether / ARP who-has 192.168.1.0/24 says 0.0.0.0
-------------------------------------------------------
Combined Packet: Ether / ARP who-has 192.168.1.0/24 says 0.0.0.0
-------------------------------------------------------
Scanning complete. Results:
-------------------------------------------------------
IP: 192.168.1.2, MAC: 00:11:22:33:44:55
-------------------------------------------------------
IP: 192.168.1.3, MAC: 66:77:88:99:AA:BB
-------------------------------------------------------

Notes

    Ensure you have the necessary permissions to scan the network.
    This script is intended for educational and personal use only.

Disclaimer

This tool is provided "as is", without warranty of any kind. The author is not responsible for any misuse or damage caused by this script.