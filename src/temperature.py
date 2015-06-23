#! /usr/bin/env python

"""this is a python module that converts temperature
"""

def f_to_k(temp):
    converted=((temp-32)*(5/9.0))+273.15
    return converted


def f_to_c(temp):
    return ((temp-32)*(5/9.0))


print(f_to_k(32))
print(f_to_k(212))
print(f_to_k(65))
