import numpy as np
import cv2

class Viewport:

    def __init__(self, focal_distance=1, shape=(500, 500), viewport_height=2.0):
        self.focal_distance = focal_distance
        self.shape = shape
        self.viewport_height = viewport_height
        self.viewport_width  = viewport_height * shape[1] / shape[0]
        self.origin = (-self.viewport_width / 2, self.viewport_height / 2)
        self.image = np.zeros((*shape, 3), dtype=np.uint8)

    def mapping(self, coordinates):
        i, j = coordinates
        x = j *  self.viewport_width / self.shape[1]  + self.origin[0]
        y = i * -self.viewport_height / self.shape[0] + self.origin[1]
        return x, y 
    
    def lightup_pixel(self, i, j, rgb):
        self.image[i, j] = np.array(rgb)

    def imshow(self):
        cv2.imshow("Image", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()   
         