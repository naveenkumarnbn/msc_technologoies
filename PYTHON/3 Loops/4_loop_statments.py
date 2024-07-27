'''
3. Loop statements 
    1. break     ==> break is used to terminates the loop
    2. continue  ==> continue is used to skipe the current iteration

'''

names = ['sri','ram','balu','ramesh','ganesh']

for name in names:
    print(name)
    if name == 'balu':
        print(' NAME IS :', name)
        break



l = [3,5,12,6,7,88,4,23]
for i in l:
    if i <= 10 : continue
    print(i)






