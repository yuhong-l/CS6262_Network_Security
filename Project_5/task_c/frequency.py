#!/usr/bin/env python3
import struct
from collections import Counter

def sorting(dictFrequency):
    result = sorted(dictFrequency.items(), reverse = True, key = lambda x: x[1] )
    return result

def frequency(payload):
    c = Counter(payload)
    
    number = 0.0
    for (k,n) in list(dict(c).items()):
        number = number + n
    #print(number)

    result = {}
    for (k,n) in list(dict(c).items()):
        result.update({k:round(n/number,3)})
    #print(result)
    return result
