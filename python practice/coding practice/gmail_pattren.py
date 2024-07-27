 # To match the gmail pattren by using regular expressions

import re
gmail = input("enter a mail id ")
ro = re.search("([a-z A-Z ])([0-9]\d+).?([a-z]\w+).([a-z]\w+)",gmail)
print(ro.group())
if ro:
    print("gmail is matched")
else:
    print("gmail is not matched")