'''
1. zip() is used to map the similar index of multiple containers and returns an zip object.
2. Using zip we can make combination of multiple listes
'''

l = [1,2,3,4,5]
l2 = ['a','b','c','d','e','f']


# crate a combination for 2 lists using zip function
zobj = zip(l, l2)
print(' zip values are :', list(zobj))

## Zip with more than two lists
zo = zip(l, l2, ['X','Y','Z'])
print(list(zo))


## Create a dictionary usnig 2 lists by using zip and dict functions
print(' zip values are :', dict(list(zip(l,l2))))









