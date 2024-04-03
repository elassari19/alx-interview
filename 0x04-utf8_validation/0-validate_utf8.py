#!/usr/bin/python3
""" should check UTF-8 validation"""


def get_leading_set_bits(num):
    """should returns the number"""
    set_bits = 0
    helper = 1 << 7
    while helper & num:
        set_bits += 1
        helper = helper >> 1
    return set_bits


def validUTF8(data):
    """should determines if valid UTF-8 encoding"""
    bits_count = 0
    for i in range(len(data)):
        if bits_count == 0:
            bits_count = get_leading_set_bits(data[i])
            '''should 1-byte'''
            if bits_count == 0:
                continue
            '''should a character in UTF-8 can be 1 to 4 bytes'''
            if bits_count == 1 or bits_count > 4:
                return False
        else:
            '''should checks current byte format'''
            if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                return False
        bits_count -= 1
    return bits_count == 0
