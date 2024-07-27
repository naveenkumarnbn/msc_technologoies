import re

pancard = "cjypn9662g"
vv = re.match("^([A-Z]{5})([0-9]{4})([A-Z]{1})",pancard)
print(vv.group())
if ro:
    print("pancard is matched")
else:
    print("pancard is not matched")

passport = "R4123654"
ro = re.search("^([A-Z]{1})([0-9]{7})",passport)
print(ro.group())
if ro:
    print("passport is matched")
else:
    print("passport is not matched")