'''
1. Search is used to find a patran any where in the string 
'''
import re

name = 'sriram123'
mo = re.search('ram', name)
print(mo.group())



