#!/usr/bin/env python3

# we can drop non-dominants

def print_items(n):
    for i in range (n):
        for j in range(n):
            print(i, j)

    for k in range (n):
        print(k)

print_items(10)
# this was O(n^2 + n)
# this can be simplified to O(n^2) because overtime n becomes
# insignifant, or "non-dominant," compared to n^2
