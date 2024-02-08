#!/usr/bin/env python3

# To understand what is happening when appending a node at the end of a list,
# such as say a value of 4 with a pointer of "None," we have to breakdown
# what even is a node.

# The node in this example is made up of two parts: a value of 4 and a pointer
# indicating "None." You can think of it as a dictionary:

# {
#  "value": 4,
#  "next": None
# }

# Preceding values deal with their pointers like this:
# {
#  "value": 7,
#  "next": {
#           "value": 4,
#           "next": None
#          }
# }

head = {
            "value": 11,
            "next": {
                     "value": 3,
                     "next": {
                              "value": 23,
                              "next": {
                                       "value": 7,
                                       "next": None
                                      }
                             }
                    }
       }

print(head['next']['next']['value'])

# This will only run with a Linked List
# print(my_linked_list.head.next.next.value)
