import numpy as np
from .hittable import Hittable
from .ray import Ray
from utils.helpers import mirror

class Scene(Hittable):

    def __init__(self, viewport, objects=[], lightbulb=(0, 0, 0), i_d=(255, 255, 255), i_s=(255, 255, 255), i_a=(255, 255, 255)):
        self.viewport = viewport
        self.objects = objects
        self.lightbulb = lightbulb
        self.i_d = np.array(i_d)
        self.i_s = np.array(i_s)
        self.i_a = np.array(i_a)

    def add(self, object):
        self.objects.append(object)

    def hit(self, ray, tmin=0.0, tmax=np.inf):
        hitted  = False
        closest = tmax
        for object in self.objects:
            if object.hit(ray=ray, tmax=closest):
                hitted = True
                self.record = object.record
                closest = self.record.t
        return hitted
    
    def color(self, ray):
        trichromatic = (0, 0, 0)
        if self.hit(ray):
            L = Ray(origin=self.record.point, direction=(self.lightbulb - self.record.point))
            R = Ray(origin=self.record.point, direction=mirror(v=L.direction, pivot=self.record.normal))
            V = -ray
            N = self.record.normal

            # lambert contribution
            lambert = np.zeros((3,))
            dot = N.T @ L.direction
            if dot >= 0:
                lambert = self.record.material.k_d * dot * self.i_d

            # specular contribution
            specular = np.zeros((3,))
            dot = V.direction.T @ R.direction
            if dot >= 0:
                specular = self.record.material.k_s * (dot ** self.record.material.alpha) * self.i_s
                
            # ambient light 
            trichromatic = lambert + specular + self.record.material.k_a * self.i_a
        return trichromatic

    def vizualize(self):
        image_height, image_width = self.viewport.shape

        for j in range(image_width):
            for i in range(image_height):
                x, y = self.viewport.mapping(coordinates=(i, j))
                ray = Ray(direction=(x, y, -self.viewport.focal_distance))
                trichromatic = self.color(ray)
                self.viewport.lightup_pixel(i, j, trichromatic)

        self.viewport.imshow()
