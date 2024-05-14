import numpy as np

class Material:

    def __init__(self, k_d, k_s, k_a, alpha=1.0):
        self.k_d = np.array(k_d)
        self.k_s = np.array(k_s)
        self.k_a = np.array(k_a)
        self.alpha = alpha