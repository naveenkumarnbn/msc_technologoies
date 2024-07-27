l = [11,23,35,66]
l2 = ['A','B','C']

# To add new value into list it will add in end of the list
l.append(4)

# To add new value based on index
l.insert(2, 99)

# clear is used to remove all the values in a list
l.clear()
print(l)

# pop is used to remove value based on index if you don't give any index it will remove last value
l3.pop(0)
print(l3)

# remove is used to delete values bases on value
l3.remove('B')

#  to sort a list in ascending order
sl = [3,5,9,2,1,7]
sl.sort()
print(sl)

#  to sort a list in descending order
sl = [3,5,9,2,1,7]
sl.sort(reverse=True)
print(sl)
