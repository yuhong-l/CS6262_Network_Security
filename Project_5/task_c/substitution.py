#!/usr/bin/env python3

import struct
import math
import dpkt
import socket
from collections import Counter
from frequency import *

def substitute(attack_payload, substitution_table):
    # Using the substitution table you generated to encrypt attack payload
    # Note that you also need to generate a xor_table which will be used to decrypt
    # the attack_payload
    # i.e. (encrypted attack payload) XOR (xor_table) = (original attack payload)
    b_attack_payload = bytearray(attack_payload, "utf8")
    result = []
    xor_table = []
    # Based on your implementattion of substitution table, please prepare result
    # and xor_table as output

    return (xor_table, result)

def getSubstitutionTable(artificial_payload, attack_payload):
    # You will need to generate a substitution table which can be used to encrypt the attack
    # body by replacing the most frequent byte in attack body by the most frequent byte in
    # artificial profile one by one

    # Note that the frequency for each byte is provided below in dictionay format.
    # Please check frequency.py for more details
    artificial_frequency = frequency(artificial_payload)
    attack_frequency = frequency(attack_payload)

    sorted_artificial_frequency = sorting(artificial_frequency)
    sorted_attack_frequency = sorting(attack_frequency)

    # Your code here ...

    
    # Make sure your substitution table can be used in
    # substitute(attack_payload, subsitution_table)
    print(substitution_table)
    return substitution_table


def getAttackBodyPayload(path):
    f = open(path, 'rb')
    pcap = dpkt.pcap.Reader(f)
    for ts, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data
        if socket.inet_ntoa(ip.dst) == "192.150.11.111": 
            tcp = ip.data
            if tcp.data == "":
                continue
            return tcp.data.rstrip()

def getArtificialPayload(path):
    f = open(path, 'rb')
    pcap = dpkt.pcap.Reader(f)
    for ts, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data
        tcp = ip.data
        if tcp.sport == 80 and len(tcp.data) > 0:
            return tcp.data
