'''
1. Using inheritance we can get parent class properties into child class.
'''
class A():
    name = 'SRIRAM'          # CLASS VARIABLE

    def add(self):
        print(' ADD IS : ')

    def sub(self):
        print(' SUB IS : ')

class Arth_Oper(A):
    def mul(self):
        print(' ADD IS : ')

    def dev(self):
        print(' DEV IS : ')

inst = Arth_Oper()
inst.add()
print(inst.name)
