#!/usr/bin/python3.4
from num2words import num2words

print("Give a number")
nums = input()

ke = num2words(nums)
se = num2words(nums, to='ordinal')
ge = num2words(nums, lang='pt')

print(ke , se  , ge)
