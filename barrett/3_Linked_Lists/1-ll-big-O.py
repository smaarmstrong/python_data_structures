#!/usr/bin/env python3

# Appending a new node to the end of the list is O(1)
# because it doesn't matter how many nodes are in the list;
# it takes the same number of operations to add it to the end

# Removing a node from the end of a linked list is more complicated
# than what you have in an array. We have to set the pointer
# to equal a different pointer, the penultimate one. It requires
# you to iterate through an entire list therefore it is O(n).

# To add a node to the start, we have to make the head point to the 
# new node. It doesn't matter how many nodes are in the linked list
# because this is O(1). 

# Decapitating is O(1) because it doesn't require iteration.

# Inserting in the middle of a list is going to be O(n) because it
# requires iteration.

# In short, anything requiring iteration is O(n) while appending & 
# deleting/inserting at the start is O(1).
