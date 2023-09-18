#!/usr/bin/env python3

# dictionaries use memory addresses differently from ints

dict1 = {
        'value': 11
        }
dict2 = dict1

print(dict1)
print(dict2)
print(id(dict1))
print(id(dict2))

dict2['value'] = 22
print(dict1)
print(dict2)
print(id(dict1))
print(id(dict2))

dict3 = {
        'number': 23
        }
print(dict1)
print(dict2)
print(dict3)
print(id(dict1))
print(id(dict2))
print(id(dict3))

dict2 = dict3
print(dict1)
print(dict2)
print(dict3)
print(id(dict1))
print(id(dict2))
print(id(dict3))
