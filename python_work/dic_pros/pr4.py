"""
The task of finding the sum of all items in a dictionary in Python involves calculating the total of all values stored in a dictionary.

For example, given a dictionary {‘a’: 100, ‘b’: 200, ‘c’: 300}, the sum of values would be 100 + 200 + 300 = 600
"""

# dk = {key:value for key,value in zip(("a","b","c"),(100,200,300))}
#
# # sum_values = sum(list(dk.values()))
# # print(sum_values)

a = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# out = [[key,a[key]] for key in a.keys()]
# print(out)

out1 = list(map(lambda x:[x,a[x]], a.keys()))
print(out1)