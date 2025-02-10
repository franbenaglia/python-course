class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
    
x = MyClass()
print(x.i)
print(x.f())
    
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

z = Complex(3.0, -4.5)
z.r, z.i
print(z.r)
print(z.i)

