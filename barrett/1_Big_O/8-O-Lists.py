#!/usr/bin/env python3

# suppose a list...
o_list = [11, 3, 23, 7]

# these operations are O(1)
o_list.append(17)
o_list.pop()

# doing this requires re-indexing because 3, 23, 7 are no longer 1, 2, 3
# due to 0 getting popped and inserted, therefore these operations are
# O(n)
o_list.pop(0)
o_list.insert(0, 11)

# so adding or removing (append(n) or pop()) at the end is O(1)
# adding or removing at the beginning is O(n) because of reindexing

# same for middle of the list, this is O(n) because of the reindexing
o_list.insert(1, 'Hi')
o_list.pop(1)

# iterating through a list to find a number is O(n)
# going directly to the place in the list i.e. o_list[2]
# is O(1)
