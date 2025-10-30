from dataclasses import dataclass

@dataclass(frozen = True)
class Color:
    r: int = 0
    g: int = 0
    b: int = 0
    
    def get_normalized(self):
        return (self.r / 255, self.g / 255, self.b / 255)
    
    def to_tuple(self) -> tuple:
        return (self.r, self.g, self.b)

RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
WHITE = Color(255, 255, 255)
BLACK = Color(0, 0, 0)
SAND = Color(194, 178, 128)