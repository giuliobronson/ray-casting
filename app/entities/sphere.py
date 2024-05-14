import numpy as np
from .hittable import Hittable, Record

class Sphere(Hittable):

    def __init__(self, material, center=(0, 0, 0), radius=1.0):
        self.material = material
        self.center = np.array(center)
        self.radius = radius

    def hit(self, ray, tmin=0.0, tmax=np.inf):
        co = ray.origin - self.center 
        a = ray.direction.T @ ray.direction
        b = 2.0 * ray.direction.T @ co
        c = co.T @ co - self.radius ** 2
        delta = b ** 2 - 4 * a * c

        if delta < 0: 
            return False
        
        t = (-b - np.sqrt(delta)) / (2 * a)
        if t <= tmin or t >= tmax:
            t = (-b + np.sqrt(delta)) / (2 * a)
            if t <= tmin or t >= tmax:
                return False
        
        closest = ray.at(t)
        normal = (closest - self.center) / self.radius
        self.record = Record(point=closest, normal=normal, t=t, material=self.material)
        return True
