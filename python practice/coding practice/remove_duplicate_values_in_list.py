# removing the duplicate elements
l = [12,2,5,2,12,2,6,5]
#def fun(l):
nl = []
for i in l:
    if i not in nl:
        nl.append(i)
print(nl)
#k = fun(l)
#print(k)
                #op [12,2,5,6]...........