'''
1. If you inheritance more than one class that is called multi inheritance
'''
class One():
    def add(self, a, b):
        print('ADD is : ', a + b)

class Two():
    def sub(self, a, b):
        print('SUB is : ', a - b)

class Arth_Oper(One, Two):
    def mul(self, a, b):
        print('MUL is : ', a * b)

inst = Arth_Oper()
inst.mul(3, 10)
inst.add(5, 6)
inst.sub(5, 6)
