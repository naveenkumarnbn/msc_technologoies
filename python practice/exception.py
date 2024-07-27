try:
 a=0
  b=10
  c=b/a # ZeroDivisionError

 l='name'
 i={'name':'ram','eid':26}
 print(i['id'])  # key error

 print(ramesh)   # name error

 result = '10' + 5 # type error

 a=int('$')  # value error

 def add():
     a=100
          b=200
 print(add)    # IndentationError

file=open(r'demo.txt')  #FileNotFoundError

l=[1,2,3,4]
 print(l[4]) #IndexError
 except exception as e:
 print(e)

 # except zero divisional error  as e:
 # print(e)

 except exception as k:
  print(k)

 except exception as n:
   print(n)

 except exception as t:
   print(t)

 except exception as id:
   print(id)

 except exception as fh:
   print(fh)

 except exception as ie:
   print(ie)

 else:
    print("the condition is successful")

 finally:
     print("clean up process")