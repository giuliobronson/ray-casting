from entities.scene import Scene
from entities.viewport import Viewport
from entities.sphere import Sphere
from entities.material import Material

if __name__ == "__main__":
    # defining a material
    material = Material(
        k_d=(0.45, 0, 0), 
        k_s=(0.45, 0.45, 0.45), 
        k_a=(0.1, 0.1, 0.1), 
        alpha=100
    )

    # setting scene
    scene = Scene(viewport=Viewport(), lightbulb=(0, 2, 0))
    scene.add(Sphere(material=material, center=(0, 0, -2), radius=1.0))

    # vizulization
    scene.vizualize()
