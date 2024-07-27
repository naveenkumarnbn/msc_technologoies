'''
1. using iterators we can get sequence of values based on demand using next() function.
'''

l = [1,2,3,4,5]

#for i in l:
#    print(i)

iter_obj = iter(l)
print(next(iter_obj))
print(next(iter_obj))


for i in iter_obj:
    print(' For loop ', i)
