import re
s = "hai@# ramu@%$"
r = re.sub('\W+',' ',s)
print(r)