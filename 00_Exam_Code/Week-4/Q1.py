# 1. Write a Python program using the math module to perform the following for a given
# number:
# • Find its square
# • Find its cube
# • Find its square root
# (Use appropriate math functions.)

import math

num = int(input("Enter a number: "))

squ = math.pow(num, 2)
cube = math.pow(num, 3)
squ_root = math.sqrt(num)

print(f"The square of {num} is {squ}")
print(f"The cube of {num} is {cube}")
print(f"The square root of {num} is {squ_root}")