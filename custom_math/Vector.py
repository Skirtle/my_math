from dataclasses import dataclass, field
import math

PI = 3.141592654

@dataclass
class Vector2:
    x: float = 0
    y: float = 0
    
    
    # Mathy methods
    def __neg__(self) -> "Vector2": return Vector2(-self.x, -self.y)
    def __bool__(self): return not (self.x == 0 and self.y == 0)
    
    def __eq__(self, other: object) -> bool: 
        if (not isinstance(other, Vector2)): return NotImplemented
        return self.x == other.x and self.y == other.y
    
    def __add__(self, other: object) -> "Vector2":
        if (not isinstance(other, Vector2)): return NotImplemented
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: object) -> "Vector2":
        if (not isinstance(other, Vector2)): return NotImplemented
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other: object) -> "Vector2":
        if (not isinstance(other, (int, float))): return NotImplemented
        return Vector2(self.x * other, self.y * other)
    
    def __truediv__(self, other: object)  -> "Vector2":
        if (not isinstance(other, (int, float))): return NotImplemented
        return Vector2(self.x / other, self.y / other)
    
    def __floordiv__(self, other: object)  -> "Vector2":
        if (not isinstance(other, (int, float))): return NotImplemented
        return Vector2(self.x // other, self.y // other)
    
    # Math but not dunder
    def magnitude(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def normal(self) -> "Vector2":
        mag = self.magnitude()
        return Vector2(self.x / mag, self.y / mag)
    
    def normalize(self) -> "Vector2":
        mag = self.magnitude()
        self.x /= mag
        self.y /= mag
        return self
    
    def dot(self, other: "Vector2") -> float:
        return (self.x * other.x) + (self.y * other.y)
    
    def proj(self, other: "Vector2") -> "Vector2":
        dot_prod = self.dot(other)
        mag_sqr = self.magnitude() ** 2
        div = dot_prod / mag_sqr
        return Vector2(self.x * div, self.y * div)
    
    # Non-math methods
    def __str__(self): return f"<{self.x}, {self.y}>"
    
    
    
def get_2d_angle(v1: Vector2, v2: Vector2, mode = "rad") -> float:
        # a.b = |a| * |b| * cos(theta)
        # a.b / (|a| * |b|) = cos(theta)
        # theta = arccos(a.b / (|a| * |b|))
        
        if (mode.lower() not in ["rad", "deg"]): return NotImplemented
        
        v1_mag = v1.magnitude()
        v2_mag = v2.magnitude()
        dot_prod = v1.dot(v2)
        
        if (dot_prod == (v1_mag * v2_mag)): # Angle is 0 deg
            return 0
        elif (dot_prod == -(v1_mag * v2_mag)): # Angle is 180 deg
            return PI if mode == "rad" else 180
        
        rads = math.acos(dot_prod / (v1_mag * v2_mag))
        
        return rads if mode == "rad" else rads * 180 / PI