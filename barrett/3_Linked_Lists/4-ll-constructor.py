#!/usr/bin/env python3

# the class for creating nodes
# only contains a constructor method
class Node:
    def __init__(self, value): # "self" is how you tell this is a method inside of a class instead of a function
        self.value = value
        self.next = None

# the Linked List constructor class method takes
# the Node value and passes it into the new LinkedList object
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

my_linked_list = LinkedList(4)

print(my_linked_list.head.value)
