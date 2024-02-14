#!/usr/bin/env python3

def print_list(self):
    temp = self.head # this starts the counter at the head
    while temp is not None: # in other words, when we haven't reached the end of the list
        print(temp.value)
        temp = temp.next # this is the equivalent of something like counter++
