#!/usr/bin/env python3

# What is big O, Omega, and Theta in the context of programming? Provide a real world example of them.

# Worst, Best, and Average case scenarios in terms of time and space complexity. 
# From the beginning of iterating through a list, finding x at the start is omega,
# middle is theta, and end is big O.

# What is time complexity? 
# Number of operations in an algorithm.

# What is space complexity?
# Memory needed to perform the operations.

# What is the second worst O case? Write an example of it.
# O(n) NEED AN EXAMPLE!!!

#def print_items(n):

    # O(n) because it ran n times
#    for i in range(n):
#        print(i)

#print_items(10)

# How can we simplify O(2n)? Write an example of O(2n).
# Drop the constant to O(n).

#def print_items(n):
#    for i in range (n):
#        print(i)

#    for j in range(n):
#        print(j)

#print_items(10)
# this ran O(n + n) or O(2n) times
# we can drop the constant (2) and say it is still O(n)

# What is the least efficient O case?
# O(n^2)

#def print_items(n):
#    for i in range (n):
#        for j in range(n):
#            print(i, j)

#print_items(10)

# this printed O(n * n) times or O(n^2)

# How can we simplify O(n^2 + n)? Write an example of O(n^2 + n).
# we can drop non-dominants

#def print_items(n):
#    for i in range (n):
#        for j in range(n):
#            print(i, j)

#    for k in range (n):
#        print(k)

#print_items(10)
# this was O(n^2 + n)
# this can be simplified to O(n^2) because overtime n becomes
# insignifant, or "non-dominant," compared to n^2

# What is the most efficient O case? What is this case also known as? 
# Write an example of this case.
# O(1), the most efficient case, is known as constant time. 

#def add_items(n):
#    return n + n
    # return n + n +n is still O(1)

# What is the second best O case? 
# O(log n)

# What is the O case occasionally used for sorting algorithms?
# O(n log n) or something like that.

# Write an example of O(n).
#def print_items(n):
#    for i in range(n):
#        print(i)

#    for j in range(n):
#        print(j)

# Write an example of O(a + b).

#def print_items(a, b):
#    for i in range(a):
#        print(i)

#    for j in range(b):
#        print(j)

# Write an example of O(a * b).

#def print_items(a, b):
#    for i in range(a):
#        for j in range(b):
#            print(i, j)

# List two examples of list operations that are O(1). Why are they O(1)?
# list.pop() and list.append()
# they go directly to the place in the list

# List two examples of list operations that are O(n). Why are they O(n)?
#o_list.pop(0)
#o_list.insert(0, 11)
# they require re-indexing

# When you iterate through a list to find an item, what O case is that?
# iterating through a list to find a number is O(n)

# When you find an item through o_list[n], what O case is that?
# O(1) because it goes directly to the item in the list

# Suppose n = 100, what do the big 4 O cases equal?
# O(1) = 1
# O(log n) ≈ 7
# O(n) = 100
# O(n^2) = 1,000,000
# this is a way of visualizing the efficiency between these O cases

# Describe the big 4 O cases with only a few words.
# O(n^2) is a loop within a loop
# O(n) is proportional
# O(log n) is divide and conquer
# O(1) is constant time

# What is a good reference website for O cases?
# www.bigocheatsheet.com
