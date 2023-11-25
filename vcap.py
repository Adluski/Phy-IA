from manim import *

class SphericalCapVolume(ThreeDScene):
    def construct(self):
        # Define the sphere and spherical cap parameters
        R = 3  # Radius of the sphere
        h = 1  # Height of the spherical cap
        a = (R**2 - (R - h)**2)**0.5  # Radius of the base of the spherical cap

        # Create the sphere
        sphere = Sphere(radius=R).set_color(WHITE).set_opacity(0.5)

        # Create the circle to represent the base of the spherical cap
        cap_base = Circle(radius=a).set_fill(RED, opacity=0.5).move_to(UP*(R - h))

        # Display text and formulas
        volume_text = MathTex(r"V = \frac{1}{3}\pi h^2 (3R - h)", color=WHITE).to_edge(UP)
        volume_formula = MathTex(r"V = \frac{1}{6}\pi h (3a^2 + h^2)", color=WHITE).next_to(volume_text, DOWN)

        # Add the sphere and the cap to the scene
        self.add(sphere)
        self.add(cap_base)
        self.add(volume_text)
        self.add(volume_formula)

        # Set the camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.wait(5)
