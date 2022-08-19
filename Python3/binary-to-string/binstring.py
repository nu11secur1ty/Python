#!/usr/bin/python
# Binary string to be converted
binary_string = "01110000 01111001 01110100 01101000 01101111 01101110"
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
