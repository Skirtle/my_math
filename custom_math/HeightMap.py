from dataclasses import dataclass

@dataclass
class HeightMap:
    size: int
    default_value: float = 0.0
    
    def __post_init__(self):
        self.map = [[self.default_value for i in range(self.size)] for j in range(self.size)]