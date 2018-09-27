class Cal(object):
    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2
    def add(self):
        return self.v1+self.v2
    def subtract(self):
        return self.v1-self.v2
    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v
    def getV1(self):
        return self.v1

class CalMul(Cal):
    def multiply(self):
        return self.v1*self.v2

class CalDivide(CalMul):
    def divide(self):
        return self.v1/self.v2

c1 = CalMul(10,10)
print(c1.add())
print(c1.subtract())
print(c1.multiply())

c2 = CalDivide(20,10)
print(c2.add())
print(c2.subtract())
print(c2.multiply())
print(c2.divide())

# c1.setV1('one')
# c1.v2 = 30
# print(c1.add())
# print(c1.subtract())
