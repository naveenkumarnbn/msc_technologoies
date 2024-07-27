import re
passport = "R4123654"
ro = re.search("^([A-Z]{1})([0-9]{7})",passport)
print(ro.group())
if ro:
    print("passport is matched")
else:
    print("passport is not matched")

