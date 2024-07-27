import re
ip = '146.111.123.12'
ro = re.search("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",ip)
print(ro.group())
if ro:
    print("ip is matched")
else:
    print("ip is not matched")
