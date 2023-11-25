from manim import *

class DS(ThreeDScene):
    def construct(self):
        # Create a sphere
        sphere = Sphere()

        # Set the color and glossiness of the sphere
        sphere.set_color(BLUE_E)
        sphere.set_gloss(0.8)

        # Add the sphere to the scene
        self.add(sphere)

        # Rotate the sphere
        self.play(Rotate(sphere, angle=PI/2, axis=UP))

        # Show the scene
        self.wait(2)
