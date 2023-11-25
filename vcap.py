from manim import *

class SphericalCapVolume(ThreeDScene):
    def construct(self):
        # Define the sphere and spherical cap parameters
        R = 3  # Radius of the sphere
        h = 1  # Height of the spherical cap
        a = (R**2 - (R - h)**2)**0.5  # Radius of the base of the spherical cap
        
        # Create the sphere
        sphere = Sphere(radius=R).set_color(WHITE).set_opacity(0.2)
        
        # Create the circle to represent the base of the spherical cap
        cap_base = Circle(radius=a).set_stroke(BLUE, opacity=0.8).move_to(UP*(R - h))
        
        # Create a filled circle to represent the spherical cap volume
        cap_volume = Dot(point=UP*(R - h), radius=a).set_color(RED).set_opacity(0.5)

        # Display text and formulas
        volume_text = MathTex(r"V = \frac{1}{3}\pi h^2 (3R - h)").to_edge(UP)
        volume_formula = MathTex(r"V = \frac{1}{6}\pi h (3a^2 + h^2)").next_to(volume_text, DOWN)

        # Animate the creation of the sphere and the cap
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.play(FadeIn(sphere), ShowCreation(cap_base))
        self.wait(1)
        self.play(TransformFromCopy(cap_base, cap_volume))
        self.wait(1)

        # Show the volume formulas
        self.play(Write(volume_text), Write(volume_formula))
        self.wait(2)

        # Clear the scene
        self.play(FadeOut(sphere), FadeOut(cap_base), FadeOut(cap_volume), FadeOut(volume_text), FadeOut(volume_formula))
        self.wait(1)
