#!/usr/bin/env python3

# this is the least efficient worst case in terms of
# time and space complexity

def print_items(n):
    for i in range (n):
        for j in range(n):
            print(i, j)

print_items(10)
# this printed O(n * n) times or O(n^2)
