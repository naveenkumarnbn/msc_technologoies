n = 1
bl = 0
l = 0
for i in range(1,10):
    bl = l
    l = n
    n = bl+l
print(n)

#using  loops

# def fib(n):
    # if n==1:
        # return 1
    # elif n==2:
        # return 1
    # elif n>2:
        # return fib(n-1)+fib(n-2)
# for n in range(1,10):
    # print(n,":",fib(n))
