import numpy as np

def mirror(v, pivot):
    normal = np.array(pivot) / np.linalg.norm(pivot)
    target = np.array(v)

    target_n = (target.T @ normal) * normal
    target_t = target - target_n

    return target_n - target_t
