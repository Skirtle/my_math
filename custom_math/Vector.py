from dataclasses import dataclass, field
import math

@dataclass
class Vector2:
    x: float = 0
    y: float = 0
    
    
    # Mathy methods
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
    
    # Non-math methods
    def __bool__(self): return not (self.x == 0 and self.y == 0)
    def __str__(self): return f"<{self.x}, {self.y}>"