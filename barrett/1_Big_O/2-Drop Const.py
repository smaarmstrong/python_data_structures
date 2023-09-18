#!/usr/bin/env python3

# we can simplify to O(n) by dropping constants

def print_items(n):
    for i in range (n):
        print(i)

    for j in range(n):
        print(j)

print_items(10)
# this ran O(n + n) or O(2n) times
# we can drop the constant (2) and say it is still O(n)
