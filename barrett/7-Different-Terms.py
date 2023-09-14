#!/usr/bin/env python3

def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

# the above code is O(n)

def print_items(a, b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)

# the above code appears to be O(n + n), O(2n), or O(n) (same thing)
# but it is actually O(a + b), so don't be mistaken!

def print_items(a, b):
    for i in range(a):
        for j in range(b):
            print(i, j)

# similarly, this is O(a * b)
