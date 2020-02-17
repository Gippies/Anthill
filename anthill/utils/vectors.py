import math


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    def __add__(self, other):
        return Vector2(int(self.x + other.x), int(self.y + other.y))

    def __sub__(self, other):
        return Vector2(int(self.x - other.x), int(self.y - other.y))

    def __mul__(self, other):
        return Vector2(int(self.x * other), int(self.y * other))

    def __truediv__(self, other):
        return Vector2(round(self.x / other), round(self.y / other))

    @staticmethod
    def zero():
        return Vector2(0, 0)

    def get_normal(self):
        return math.sqrt(self.x ** 2.0 + self.y ** 2.0)

    def get_normalized_vector(self):
        normal = self.get_normal()
        if normal > 0:
            return self / self.get_normal()
        else:
            return Vector2.zero()
