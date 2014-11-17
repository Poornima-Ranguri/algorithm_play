#! /usr/bin/env python
# python_kmp.py
# David Prager Branner
# 20141117

def find(s, substring):
    # build table of shift amounts
    length = len(substring)
    shift = 1
    shift_table = [shift for _ in range(length + 1)]
    print(shift_table)
    for i in range(length):
        while shift <= i and substring[i] != substring[i - shift]:
            shift += shift_table[i - shift]
        shift_table[i + 1] = shift
        print(shift_table)
    index_start = 0
    len_match = 0
    for char in s:
        while len_match == length or \
              len_match >= 0 and substring[len_match] != char:
            index_start += shift_table[len_match]
            len_match -= shift_table[len_match]
        len_match += 1
        if len_match == length:
            yield index_start

