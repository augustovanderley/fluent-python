from math import hypot

class Vector():
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __abs__(self):
        return hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))


    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

v1 = Vector(2,4)
v2 = Vector(2,1)

assert v1 + v2 == Vector(4,5)

v = Vector(3,4)
assert abs(v) == 5.0

assert v * 3 == Vector(9,12)
assert abs(v*3) == 15.0
