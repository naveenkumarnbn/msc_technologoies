def dec_fun(f):
   def wrap_fun(name):
       return f(name).upper()
   return wrap_fun

#@dec_fun
def get_name(name):
   return name

r = get_name('sriram')
print(r)



