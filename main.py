import custom_math as c_math

def map_to(value: float, old_start: float, old_end: float, new_start: float, new_end: float) -> float:
    return new_start + (new_end - new_start) * ((value - old_start) / (old_end - old_start))

if __name__ == "__main__":
    ...