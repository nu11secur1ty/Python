#!/usr/bin/python3.4
# author @nu11secur1ty
from num2words import num2words

# Give a number
print("Give a number")
nums = input()

# Give a language
print("Lang")
taeba = input()

ke = num2words(nums)
se = num2words(nums, to='ordinal')
ge = num2words(nums, lang=taeba)

print(ke , se  , ge)
