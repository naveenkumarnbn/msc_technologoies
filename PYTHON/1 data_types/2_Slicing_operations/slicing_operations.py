'''
1. Using slicing operation we can get range of values from list.
'''

l = [7,89,34,2,5,12,99]

# To get  values 89, 34, 2, 5
print(' \n ', l[1:5])

# To get  values 34, 2, 5, 12
print(' \n ', l[2:6])

# To get  values 89, 34, 2, 5, 12, 7
print(' \n ', l[1:70])

#  To get values from 3rd index to last
print(' \n ', l[3:])

#  To get values from starting to 4th index
print(' \n ', l[:5])

#  To get all the values
print(' \n ', l[:])
 
# To get values one after another one
print(' \n ', l[::2])

# To get list values in reverse order
print(' \n ', l[::-1])


s = 'SRIRAM'
# TO get first charecter from string
print(s[0])

# TO REVERSE A STRING USING SLICING OPERATION
print(s[::-1])






