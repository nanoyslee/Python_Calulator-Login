class C(object):
    def __init__(self, v):
        self.inst_value = v
    def getValue(self):
        return self.inst_value
    def setValue(self, v):
        self.inst_value = v

c1 = C(10)
print(c1.getValue())
c1.setValue(20)
print(c1.getValue())
