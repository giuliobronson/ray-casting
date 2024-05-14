import numpy as np

class Ray:

    def __init__(self, origin=np.array((0, 0, 0)), direction=np.array((0, 0, 0))):
        self.origin = np.array(origin)
        self.direction = np.array(direction) / np.linalg.norm(direction)

    def at(self, t):
        return self.origin + t * self.direction
    
    def __neg__(self):
        return Ray(origin=self.origin, direction=-self.direction)
