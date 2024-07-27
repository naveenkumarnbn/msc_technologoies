'''
1. Using decorators, we can change the behavior of another function without changing any code.
2. using @ (symbol) we can assign a decorator to the function.

## Decoraor function creation principles
    1. Decorator function takes input argument as function
    2. Decorator function contains another wrapper function.
    3. Inside wrapper function only we have to call function argument.
    4. Decorator function will return wrapper function.

'''

## SAMPLE DECORATOR TO CONVERT RETURN VALUE INTO UPPER CASE
def dec_fun(f):
    def wrap_fun():
        rv = f()
        return rv.upper()
    return wrap_fun

@dec_fun
def get_name():
    return 'sriram'

print(get_name())


## DECORATOR WITH PARAMETERS(ARGUMENTS)
def dec_fun(f):
    def wrap_fun(name):
        rv = f(name)
        return rv.upper()
    return wrap_fun

@dec_fun
def get_name(name):
    return name

print(get_name('sriram'))








