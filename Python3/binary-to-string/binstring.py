#!/usr/bin/python
# Binary string to be converted
# nu11secur1ty

binary_string = "01101110\
 01100001 00100000 01101101 01100001 01101001\
  01101011 01100001 00100000 01110110 01101001\
   00100000 01110000 01110101 01110100 01101011\
    01100001 01110100 01100001"
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
