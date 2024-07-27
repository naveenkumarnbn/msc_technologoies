# factorial "means The product of an integer and all  the integers below it"

# n = int(input("enter a number:"))
# fact = 1
# while(n>0):
    # fact = fact * n
    # n = n - 1
# print("factorial value is:",fact)

###        6 factorial value is 720            #######

def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f
d = fact(6)
print(d)