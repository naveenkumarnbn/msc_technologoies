l=[3,2,3,5,5,3,7,6,4,6,7,2]

print ('\nelements are:\t',l)

count_dict={}

for i in l:

    count_dict[i]=l.count(i)

print ('\nfrequency:\t',count_dict)

print('\nkeys:\t',count_dict.keys())

print('\nvalues:\t',count_dict.values())



# l = [1,1,2,2,5,5,4,4,3,2,5]
# print(l.count()) 			   must give one argument