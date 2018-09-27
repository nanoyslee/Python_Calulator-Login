class Cs:
    @staticmethod
    def static_method():
        print("Static Method")
    @classmethod
    def class_method(cls):
        print("Class Method")
    def instance_method(self):
        print("Instance Method")

i = Cs()
Cs.static_method()
Cs.class_method()
i.instance_method()
