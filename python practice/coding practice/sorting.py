s = [-12,3,-100,100,5,4,6,-16]
nl = []
for i in range(len(s)):
    a = min(s)
    nl.append(a)
    s.remove(a)
print(nl)
