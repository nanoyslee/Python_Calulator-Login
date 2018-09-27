class C(object):
    def __init__(self, v):
        self.inst_value = v

c1 = C(10)
print(c1.inst_value)
c1.inst_value = 20
print(c1.inst_value)

# how to access instance variables in the Method
# class C(object):
#     def __init__(self, v):
#         self.inst_value = v
#     def show(self):
#         print(self.inst_value)
#
# c1 = C(10)
# c1.show()
