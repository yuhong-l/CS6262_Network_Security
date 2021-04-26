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


    ## TEST for small frequency
    #artificial_payload = 'abbcccddddeeeee' 
    #attack_payload = 'rrssstttt' 

    # Note that the frequency for each byte is provided below in dictionay format.
    # Please check frequency.py for more details
    artificial_frequency = frequency(artificial_payload)
    attack_frequency = frequency(attack_payload)

    sorted_artificial_frequency = sorting(artificial_frequency)
    sorted_attack_frequency = sorting(attack_frequency)

    print("sorted aritifical ")
    print(sorted_artificial_frequency)

    print("sorted attack")
    print(sorted_attack_frequency)

    # Your code here ...    
    #print("put something here")


    #number of distint characters in attack traffic
    attack_len = len(sorted_attack_frequency);
    print(attack_len)

    #number of distincy characters in  normal/artificial
    normal_len = len(sorted_artificial_frequency);
    print(normal_len)


    #copy of attack traffic that will be substitued and becom
    #substituio_table

    temp_sub_table = sorted_attack_frequency;

    temp_values = [[] for i in range(attack_len)]


    
    for i in range(attack_len):
        #print("i is "  + str(i))
        #print("i val is " + str(sorted_artificial_frequency[i]))
        temp_values[i].append(sorted_artificial_frequency[i])



    #print("temp values to copy are " + str(temp_values))

    #copy temp values into original table

    substitution_table = {}
    for i in range(len(temp_sub_table)):
        temp_total = temp_sub_table[i]   #ex ('t',.44) , need to get t and place in new table
        temp_key= temp_total[0];
        temp_val = temp_total[1]
        substitution_table[temp_key]=temp_values[i]


    #now after subing first attack_len values, get the attack_len +1 character
    #and find the max ratio

    #print("current sub table is "  + str(substitution_table))

    values_left = normal_len-attack_len;
    for j in range(values_left):
        #print("*************iteration for : " +str(j))
        temp_list_comparison = {}
        largest_ration = 0
        largest_ration_key = '';
        largest_ration_value = 0;

        for i in range(attack_len):
            #get the original frequency/ divide by new frequency
            original_freq = (sorted_attack_frequency[i])[1]
            original_key =  (sorted_attack_frequency[i])[0]
            #print("original freq is "  + str(original_freq))
            #print("original freq key is "  + str((sorted_attack_frequency[i])[0]))
            #print("iterat through " + str(substitution_table[original_key]))
            #this needs to be the sum of all of them in the list
            total =0;
            for k in range(len(substitution_table[original_key])):
                #print("getting value " + str(((substitution_table[original_key])[k])[1]))
                total += ((substitution_table[original_key])[k])[1]
            #print("new freq is " + str(substitution_table[original_key]))
            #print("new freq is "  + str(total))
            new_freq = total;
            #new_freq =((substitution_table[original_key])[0])[1]
            #rint("new freq is "  + str(new_frequency))
            #print("divding " + str(original_freq) + "/" + str(new_freq))
            comparison = round(original_freq/new_freq,3);
            #print("division is " + str(comparison))
            if comparison > largest_ration :
                largest_ration_key = original_key
                largest_ration_value = comparison;
                #print("setting current largest to " + str(largest_ration_key) +":"+str(largest_ration_value))
                largest_ration = comparison;

            temp_list_comparison[original_key] = comparison;


        #print("final comparison list is " + str(temp_list_comparison))

        #print("largest ration = "  + str(largest_ration_key))
        #print("largest key  = " + str(largest_ration_value))
        #print(str(substitution_table[largest_ration_key]))
        substitution_table[largest_ration_key].append(sorted_artificial_frequency[attack_len +j])


    
    # Make sure your substitution table can be used in
    print("final")
    print(substitution_table)
    #substitute(attack_payload, subsitution_table)


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
