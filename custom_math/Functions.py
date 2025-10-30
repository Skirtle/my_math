def map_to(value: float, old_start: float, old_end: float, new_start: float, new_end: float) -> float:
    return new_start + (new_end - new_start) * ((value - old_start) / (old_end - old_start))

def lerp(x: float, start: float, end: float) -> float:
    if (x < 0 or x > 1): raise ValueError
    return x * (end - start)

def lerp_2d(x: float, x0: float, y0: float, x1: float, y1: float) -> float:
    return y0 + (x - x0) * ((y1 - y0) / (x1 - x0))

def norm(x: float, start: float, end: float) -> float:
    return map_to(x, start, end, 0, 1)