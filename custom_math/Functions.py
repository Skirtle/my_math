import math

def map_to(value: float, old_start: float, old_end: float, new_start: float, new_end: float) -> float:
    return new_start + (new_end - new_start) * ((value - old_start) / (old_end - old_start))

def lerp(x: float, start: float, end: float) -> float:
    if (x < 0 or x > 1): raise ValueError
    return x * (end - start)

def lerp_2d(x: float, x0: float, y0: float, x1: float, y1: float) -> float:
    return y0 + (x - x0) * ((y1 - y0) / (x1 - x0))

def norm(x: float, start: float, end: float) -> float:
    return map_to(x, start, end, 0, 1)

def cdf(x: float) -> float:
    return (1 + math.erf(x / (2 ** 0.5))) / 2

def get_probability(n: int, k: int, p0: float) -> dict[str,float]:
    probs = {}
    
    ph = k / n
    standard_eror = ((p0 * (1 - p0)) / n) ** (1/2)
    z_score = (ph - p0) / standard_eror
    p_score_2_sided = 2 * (1 - cdf(abs(z_score)))
    
    probs["samples"] = n
    probs["successes"] = k
    probs["sample_rate"] = ph
    probs["null_hypothesis"] = p0
    probs["standard_error"] = standard_eror
    probs["z_score"] = z_score
    probs["p_value_2_sided"] = p_score_2_sided
    
    
    return probs