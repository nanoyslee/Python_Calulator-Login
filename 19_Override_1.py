class C1(object):
    def m(self):
        return 'parents'

class C2(C1):
    def m(self):
        return super().m() + ' child'
    pass

o = C2()
print(o.m())
