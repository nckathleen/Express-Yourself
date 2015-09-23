'''Return True or False'''
import re

def binary(item):
    return re.match(r'[0-1]+',item)

def binary_even(input):
    return re.search(r'0$', input)

def hex(data):
    return re.search(r'[A-F\d]', data)

def word(a_word):
    return re.search(r'[0-9].[a-z]-+', a_word)
