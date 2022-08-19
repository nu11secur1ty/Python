#!/usr/bin/python
# Binary string to be converted
# nu11secur1ty

binary_string = input("Put here your binary ASCII/UTF8\n")
# split the above stirng using split() method by white space
binary_values = binary_string.split()
ascii_string = ""
# use for loop to iterate
for binary_value in binary_values:
    # convert to int using int() with base 2
    an_integer = int(binary_value, 2)
    # convert to character using chr()
    ascii_character = chr(an_integer)
    # merge them all
    ascii_string += ascii_character
print(ascii_string)# python
