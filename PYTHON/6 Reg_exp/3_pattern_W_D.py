import re

# + Used matches 1 or more occurrence of preceding expression.
name = 'sriram'
mo = re.search('\w+', name)
print(mo.group())


# * Used matches 0 or more occurrence of preceding expression.
name = 'sriram123'
mo = re.search('\w*', name)
print(mo.group())


# '\'   ==> Used to remove special character functionality
name = 'sri*123'
mo = re.search('sri\*123', name)
print(mo.group())