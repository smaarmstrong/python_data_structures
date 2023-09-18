#!/usr/bin/env python3

# just run this to see how pointers work with variables
# and places in memory

num1 = 22
num2 = num1
print(num1)
print(num2)
print(id(num1))
print(id(num2))
print()

num1 = 1
print(num1)
print(num2)
print(id(num1))
print(id(num2))
print()

num1 = 22
print(num1)
print(num2)
print(id(num1))
print(id(num2))
print()

num2 = 23
print(num1)
print(num2)
print(id(num1))
print(id(num2))
print()

num1 = 2
num2 = num1
print(num1)
print(num2)
print(id(num1))
print(id(num2))
print()

num1 = 22
num2 = num1
print(num1)
print(num2)
print(id(num1))
print(id(num2))
