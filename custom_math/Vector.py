from numbers import Real
from typing import Self
from math import sqrt

class Vector2:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def __add__(self, other: Self) -> Self: 
        if (not isinstance(other, Vector2)): raise TypeError(f"Expected type {Vector2.__name__}, got {type(other).__name__}")
        return Vector2(self.x + other.x, self.y + other.y)
    def __sub__(self, other: Self) -> Self:
        if (not isinstance(other, Vector2)): raise TypeError(f"Expected type {Vector2.__name__}, got {type(other).__name__}")
        return Vector2(self.x - other.x, self.y - other.y)
    def __mul__(self, scalar: Real) -> Self: 
        if (not isinstance(scalar, Real)):  raise TypeError(f"Expected type {Real.__name__}, got {type(scalar).__name__}")
        return Vector2(self.x * scalar, self.y * scalar)
    def __truediv__(self, scalar: Real) -> Self: 
        if (not isinstance(scalar, Real)):  raise TypeError(f"Expected type {Real.__name__}, got {type(scalar).__name__}")
        return Vector2(self.x / scalar, self.y / scalar)
    def __eq__(self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y
    
    def set_x(self, val: Real) -> None: self.x = val
    def set_y(self, val: Real) -> None: self.y = val
    def get_x(self) -> Real: return self.x
    def get_y(self) -> Real: return self.y
    
    def magnitude(self) -> Real: return sqrt(self.x ** 2 + self.y ** 2)
    def dot(self, other: Self) -> Real: return (self.x * other.x) + (self.y * other.y) 
    def normal(self) -> Self: 
        mag = self.magnitude()
        return Vector2(self.x / mag, self.y / mag)
        
    
    def __str__(self): return f"<{self.x},{self.y}>"
    def __repr__(self): return f"<{self.x},{self.y}>"
    
class Vector3:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
        
    def __add__(self, other: Self) -> Self: 
        if (not isinstance(other, Vector3)): raise TypeError(f"Expected type {Vector3.__name__}, got {type(other).__name__}")
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other: Self) -> Self:
        if (not isinstance(other, Vector3)): raise TypeError(f"Expected type {Vector3.__name__}, got {type(other).__name__}")
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, scalar: Real) -> Self: 
        if (not isinstance(scalar, Real)):  raise TypeError(f"Expected type {Real.__name__}, got {type(scalar).__name__}")
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)
    def __truediv__(self, scalar: Real) -> Self: 
        if (not isinstance(scalar, Real)):  raise TypeError(f"Expected type {Real.__name__}, got {type(scalar).__name__}")
        return Vector3(self.x / scalar, self.y / scalar, self.z / scalar)
    def __eq__(self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def set_x(self, val: Real) -> None: self.x = val
    def set_y(self, val: Real) -> None: self.y = val
    def set_z(self, val: Real) -> None: self.z - val
    def get_x(self) -> Real: return self.x
    def get_y(self) -> Real: return self.y
    def get_z(self) -> Real: return self.z
    
    def magnitude(self) -> Real: 
        return sqrt((self.x ** 2) + (self.y ** 2) + ( self.z ** 2))
    def dot(self, other: Self) -> Real: return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
    def normal(self) -> Self: 
        mag = self.magnitude()
        return Vector3(self.x / mag, self.y / mag, self.z / mag)
    
    def cross(self, other: Self) -> Self:
        return Vector3(self.y * other.z - self.z * other.y,
                       self.z * other.x - self.x * other.z,
                       self.x * other.y - self.y * other.x) 
        
    
    def __str__(self): return f"<{self.x},{self.y},{self.z}>"
    def __repr__(self): return f"<{self.x},{self.y},{self.z}>"

if __name__=="__main__":
    assert Vector2(1, 1) + Vector2(7, 7) == Vector2(8, 8)
    assert Vector2(2, 4) - Vector2(6, 4) == Vector2(-4, 0)
    assert Vector2(2, 4) * 2 == Vector2(4, 8)
    assert Vector2(2, 4) / 2 == Vector2(1, 2)
    assert Vector2(2, 4) != Vector2(2, 3)
    assert Vector2(2, 4) == Vector2(2, 4)
    assert Vector2(3, 4).magnitude() == 5
    assert Vector2(4, 9).dot(Vector2(3, 2)) == 30
    assert Vector2(2, 2).normal().magnitude() >= 0.99999999 and Vector2(2, 2).normal().magnitude() < 1.00000001 # Yay to floating point numbers
    
    assert Vector3(1, 1, 1) + Vector3(7, 7, 7) == Vector3(8, 8, 8)
    assert Vector3(2, 4, 8) - Vector3(6, 4, 2) == Vector3(-4, 0, 6)
    assert Vector3(2, 4, 7.5) * 2 == Vector3(4, 8, 15)
    assert Vector3(2, 4, 10.5) / 2 == Vector3(1, 2, 5.25)
    assert Vector3(2, 4, 1) != Vector3(2, 3, 1)
    assert Vector3(2, 4, 9) == Vector3(2, 4, 9)
    assert Vector3(1, 2, 2).magnitude() == 3
    assert Vector3(4, 9, 9).dot(Vector3(3, 2, 1)) == 39
    assert Vector3(2, 2, 8).normal().magnitude() >= 0.99999999 and Vector3(2, 2, 8).normal().magnitude() < 1.00000001 # Yay to floating point numbers
    assert Vector3(4, 5, 2).cross(Vector3(7, 1, 6)) == Vector3(28, -10, -31)