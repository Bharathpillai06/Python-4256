import math


class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # 1. Printing
    def __str__(self):
        a, b = self.a, self.b
        if b == 0:
            return str(a)
        if a == 0:
            return f"{b}i"
        if b < 0:
            return f"{a} - {-b}i"
        return f"{a} + {b}i"

    def __repr__(self):
        return f"Complex({self.a}, {self.b})"

    # 2. Arithmetic Methods
    def add(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def negate(self):
        return Complex(-self.a, -self.b)

    def subtract(self, other):
        return self.add(other.negate())

    def multiply(self, other):
        a, b, c, d = self.a, self.b, other.a, other.b
        return Complex(a * c - b * d, a * d + b * c)

    def conjugate(self):
        return Complex(self.a, -self.b)

    def inverse(self):
        denom = self.a ** 2 + self.b ** 2
        return Complex(self.a / denom, -self.b / denom)

    def divide(self, other):
        return self.multiply(other.inverse())

    # 3. Operator Overloading
    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.subtract(other)

    def __mul__(self, other):
        return self.multiply(other)

    def __neg__(self):
        return self.negate()

    def __truediv__(self, other):
        return self.divide(other)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    # 4. Convenience Methods
    def is_real(self):
        return self.b == 0

    def is_imaginary(self):
        return self.a == 0

    # 5. Geometry / Polar Form
    def magnitude(self):
        return math.sqrt(self.a ** 2 + self.b ** 2)

    def argument(self):
        return math.atan2(self.b, self.a)

    def to_polar(self):
        return (self.magnitude(), self.argument())

    @staticmethod
    def from_polar(r, theta):
        return Complex(r * math.cos(theta), r * math.sin(theta))

    def distance_to(self, other):
        return self.subtract(other).magnitude()


print("add:", Complex(4, 3).add(Complex(3, -5)))
print("multiply:", Complex(2, 3).multiply(Complex(1, 4)))
print("inverse:", Complex(1, -1).inverse())
print("to_polar:", Complex(3, 4).to_polar())
print("distance:", Complex(1, 2).distance_to(Complex(4, 6)))
