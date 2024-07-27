# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# Consider use dict()
# Solution:


n=int(input("enter a number"))
dict={}
for i in range(1,n+1):
    dict[i]=i*i
print (dict)