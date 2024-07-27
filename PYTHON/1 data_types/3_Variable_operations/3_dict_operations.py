d = {'name':'sri', 'eid':999, 'dname':'IT'}

# To remove all the values in a dictionary
d.clear()

# keys is used to get all keys in a dictionary in list format
print(d.keys())

# values is used to get all values in a dictionary in list format
print(d.values())

# update used to concordinate two dictionaries
d1 = {'name':'sri', 'eid':999, 'dname':'IT'}
d2 = {'A':1, 'B':2, 'C':3}
d1.update(d2)
print(d1)

