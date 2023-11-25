from manim import *

class SphereVolume(ThreeDScene):
    def construct(self):
        # Define the radius of the sphere
        radius = 2

        # Create a sphere with the specified radius
        sphere = Sphere(radius=radius)
        sphere.set_color(BLUE_E)
        sphere.set_gloss(0.8)

        # Calculate the volume of the sphere
        volume = (4/3) * PI * radius**3

        # Create a text object to display the volume
        volume_text = Text(f"Volume of sphere: {volume:.2f} units³", font_size=36)

        # Position the text on the screen
        volume_text.to_edge(UP)

        # Add the sphere and the text to the scene
        self.add(sphere, volume_text)

        # Rotate the sphere
        self.play(Rotate(sphere, angle=PI/2, axis=UP))

        # Show the scene
        self.wait(2)
