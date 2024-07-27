import re
Test = "My name is Ramu K"
r = re.search('.*\s(\w+)\s\w$', Test)
print(r.group(1))