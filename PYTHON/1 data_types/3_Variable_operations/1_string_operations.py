s = 'sriram'

# To convert all characters into upper letters
print(s.upper())

# To convert all characters into lower letters
print(s.lower())

# To convert first character into upper letters
print(s.title())

# split() method returns a list of strings after breaking the given string by the specified separator.
v = 'sriram=kumar=balu'
print(v.split(','))
print(v.split('a'))
print(v.split('ma'))
print(v.split())

# replace() is used to replace a value  with another value.
name = 'sriramsri sri'
print(name.replace('sri','RRR'))
print(name.replace('sri','RRR', 1))

# count is used to get repeated count of given value in a string
s = 'sriram sri'
print(s.count('r'))
print(s.count('sri'))



