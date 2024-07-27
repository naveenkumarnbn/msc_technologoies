
import re
pancard="CJYPN9662G"
nn = re.match("^([A-Z]{5})([0-9]{4})([A-Z]{1})",pancard)
print(nn.group())
if nn:
   print("pancard is matched")
else:
   print("pancard is un matched")


