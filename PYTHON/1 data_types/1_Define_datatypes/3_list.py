'''
1. List is used to store multiple values and we can do operation on each value based on index.
2. Using square brackets "[]" we can create a list

            0         1       2       3     4
names = ['sriram', 'ramu','ganesh', 999, 98.90]
            -5        -4     -3       -2   -1

'''
# To create a list
names = ['sri','kumar','balu','ram', 567, 99.9]

# To update a particular value
names[0] = 'sri kumar'
print(names)       #[sri kumar, kumar, balu, ram, 567, 99.9]

# To delete particular value in list
del names[2]
print(names)      #['sri kumar', 'kumar', 'ram', 567, 99.9]

# To delete a total list
del names
print(names)      #[total list will delete]

# To print particular value based on index
print(names[4])      # 99.9
print(names[-2])     # 567


