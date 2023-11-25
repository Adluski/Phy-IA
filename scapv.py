from manim import *

class SphericalCapVolume(Scene):
    def construct(self):
        # Constants for the sphere and cap
        R = 2  # Radius of the sphere
        h = 1  # Height of the cap
        r = np.sqrt(R**2 - (R-h)**2)  # Radius of the base of the cap

        # Create a circle to represent the sphere in 2D
        sphere_circle = Circle(radius=R).set_fill(BLUE, opacity=0.5)

        # Create an arc to represent the cap
        cap_arc = Arc(radius=R, angle=2*np.arccos((R-h)/R)).set_stroke(color=RED, width=4)
        cap_arc.shift((R-h)*UP)  # Position the arc to represent the cap

        # Line to represent the height of the spherical cap
        height_line = Line(start=cap_arc.get_bottom(), end=cap_arc.get_top(), color=YELLOW)

        # Label for the height
        height_label = MathTex("h").next_to(height_line, LEFT)

        # Radius line inside the sphere
        radius_line = Line(start=ORIGIN, end=R*RIGHT, color=PURPLE)
        radius_label = MathTex("R").next_to(radius_line, DOWN)

        # Formula for the volume of the spherical cap
        volume_formula = MathTex(
            "V = \\frac{1}{3} \\pi h^2 (3R - h)"
        ).to_edge(UP)

        # Group everything together
        cap_group = VGroup(sphere_circle, cap_arc, height_line, height_label, radius_line, radius_label)

        # Display the shapes and the formula
        self.play(Create(sphere_circle), Create(radius_line), Create(radius_label))
        self.wait(1)
        self.play(Write(volume_formula))
        self.wait(1)
        self.play(ShowCreation(cap_arc), GrowFromCenter(height_line), Write(height_label))
        self.wait(2)

# To render, use: manim -pql SphericalCapVolume.py SphericalCapVolume
