from manim import *

class SCV(ThreeDScene):
    def construct(self):
        # Parameters for the sphere and the spherical cap
        R = 3  # Radius of the sphere
        h = 1  # Height of the cap
        a = (2 * R * h - h**2)**0.5  # Radius of the base of the cap
        
        # Create a sphere
        sphere = Sphere(radius=R, resolution=(30, 30))
        sphere.set_opacity(0.5)
        
        # Create a plane to cut the sphere
        plane = Rectangle(width=2*a, height=2*a)
        plane.set_stroke(width=0)
        plane.set_fill(color=BLUE, opacity=0.5)
        plane.move_to(h * UP)

        # Create the spherical cap
        cap = Hemisphere(radius=R)
        cap.set_opacity(0.5)
        cap.set_fill(color=RED, opacity=0.5)
        cap.move_to((R-h) * UP)

        # Create labels for height (h), radius (R), and angle (theta)
        h_label = MathTex("h").next_to(cap, UP)
        R_label = MathTex("R").next_to(sphere, RIGHT)
        theta_label = MathTex("\\theta").move_to(R/2 * DOWN + R/2 * RIGHT)

        # Add the volume calculation text
        volume_formula = MathTex(
            "V = \\frac{1}{3}", "\\pi h^2", "(3R - h)"
        ).to_corner(UL).set_color_by_tex("h", YELLOW)

        # Volume of the spherical cap
        volume_value = (1/3) * PI * h**2 * (3*R - h)
        volume_text = Text(f"Volume: {volume_value:.2f} cubic units", font_size=36).next_to(volume_formula, DOWN)
        
        # Add everything to the scene
        self.add_fixed_in_frame_mobjects(volume_formula, volume_text)
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.add(sphere)
        self.play(FadeIn(plane))
        self.play(Transform(plane, cap))
        self.add_fixed_in_frame_mobjects(h_label, R_label, theta_label)
        self.wait(2)

