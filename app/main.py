from entities.scene import Scene
from entities.viewport import Viewport
from entities.sphere import Sphere
from entities.material import Material

if __name__ == "__main__":
    # defining a materials
    material_specular = Material(
        k_d=(0, 0.45, 0), 
        k_s=(0.45, 0.45, 0.45), 
        k_a=(0.1, 0.1, 0.1), 
        alpha=100
    )

    material_lambert = Material(
        k_d=(0, 0, 0.9), 
        k_s=(0, 0, 0), 
        k_a=(0.1, 0.1, 0.1)
    )

    # setting scene
    scene = Scene(viewport=Viewport(), lightbulb=(-2, 0, 0))
    scene.add(Sphere(material=material_lambert, center=(0, 0, -2), radius=1.0))

    # # vizulization
    scene.vizualize()
