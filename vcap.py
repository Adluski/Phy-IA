from manim import *

class SphericalCapVolume(ThreeDScene):
    def construct(self):
        # Parameters for the sphere and spherical cap
        R = 3  # Radius of the sphere
        h = 1  # Height of the spherical cap
        a = (R**2 - (R - h)**2)**0.5  # Radius of the base of the spherical cap

        # Create the sphere with radius R
        sphere = Sphere(radius=R).set_opacity(0.5).set_color(BLUE)

        # Create the circle to simulate the spherical cap
        cap = Circle(radius=a).set_fill(RED, opacity=0.5).set_stroke(color=RED)
        # Position the cap on top of the sphere at the correct height
        cap.shift(UP*(R-h))

        # Text and formulas to display
        volume_text = MathTex(r"V = \frac{1}{3}\pi h^2 (3R - h)").to_edge(UP)
        volume_formula_crater = MathTex(r"V = \frac{1}{6}\pi h (3a^2 + h^2)").next_to(volume_text, DOWN)

        # Animate the sphere and cap creation
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)  # Slowly rotate the camera
        self.play(ShowCreation(sphere))
        self.play(ShowCreation(cap))
        self.wait(2)

        # Show the volume formulas
        self.play(Write(volume_text), Write(volume_formula_crater))
        self.wait(2)

        # Animate the cap to show it fits into the sphere
        self.play(cap.animate.shift(DOWN*(R-h)))
        self.wait(2)
        self.play(cap.animate.shift(UP*(R-h)))
        self.wait(2)

        # Clear the scene
        self.play(FadeOut(sphere), FadeOut(cap), FadeOut(volume_text), FadeOut(volume_formula_crater))
        self.wait(2)

