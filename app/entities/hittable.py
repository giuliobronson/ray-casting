import numpy as np
from abc import ABC, abstractmethod

class Record:
    
    def __init__(self, point, normal, t, material):
        self.point = np.array(point)
        self.normal = np.array(normal)
        self.t = t
        self.material = material

class Hittable(ABC):
    
    @abstractmethod
    def hit(self, ray, tmin, tmax):
        pass
