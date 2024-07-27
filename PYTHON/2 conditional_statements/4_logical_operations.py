'''
  1. Logical operators are "and" , "or"
  2. Using logical operations we can execute a block of code based on multiple condition.

  # LOGICAL "AND" OPERATOR TABLE 
    A	B	A and B
    T	T	   T
    T	F	   F
    F	T	   F
    F	F	   F

  # LOGICAL "OR" OPERATOR TABLE
    A	B	A or B
    T	T	   T
    T	F	   T
    F	T	   T
    F	F	   F
'''
sal  = 50
dname = 'SALES'

#if sal >= 500 and dname == 'IT':
#    print(' SAL IS :: ', sal + 100)

if sal >= 500 or dname == 'IT' :
    print(' SAL IS :: ', sal + 100)
