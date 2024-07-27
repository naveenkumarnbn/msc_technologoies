## Using __init__ method we can create constructor
## Using constructor we can create instance varables.
class One:
    def __init__(self, a, b):
        self.a = a           # INSTANCE VARIABLE
        self.b = b           # INSTANCE VARIABLE

    def add(self):
        print(' Add a + b : ', self.a + self.b)

    def sub(self):
        print(' SUB a - b : ', self.a - self.b)

    def mul(self, c):
        print(' MUL a * b : ', self.a - self.b)

inst = One(20, 10)
inst.add()
inst.sub()
inst.mul(30)




