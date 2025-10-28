from custom_math import *

if __name__ == "__main__":
    v1 = Vector2(0, 4)
    v2 = Vector2(4, 0)
    
    print(get_2d_angle(v1, v2))
    print(get_2d_angle(v2, v1))