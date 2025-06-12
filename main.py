from custom_math import *

if __name__ == "__main__":
    assert Vector2(1, 1) + Vector2(7, 7) == Vector2(8, 8)
    assert Vector2(2, 4) - Vector2(6, 4) == Vector2(-4, 0)
    assert Vector2(2, 4) * 2 == Vector2(4, 8)
    assert Vector2(2, 4) / 2 == Vector2(1, 2)
    assert Vector2(2, 4) != Vector2(2, 3)
    assert Vector2(2, 4) == Vector2(2, 4)
    assert Vector2(3, 4).magnitude() == 5
        