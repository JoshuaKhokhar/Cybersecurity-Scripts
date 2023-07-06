"""
Script Name: packetSniffer.py
Author: Joshua Khokhar
Creation Date: 7/5/2023
Purpose: This script is a packet sniffer which retrieves data from the first packet and prints it out.
Instructions: To run this script, administrator privileges are requried.
"""

import socket

HOST = '127.0.0.1'

def main():

    socket_protocol = socket.IPPROTO_UDP

    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

    sniffer.bind((HOST, 0))

    print(sniffer.recv(65565))

if __name__ == '__main__':
    main()
