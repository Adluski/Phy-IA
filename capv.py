from manim import *
from manim.utils.space_ops import spherical_to_cartesian


class SphericalCapVolume(ThreeDScene):
    def construct(self):
        # Constants
        R = 2  # Radius of the sphere
        h_max = R  # Maximum height of the cap

        # Create a sphere
        sphere = Sphere(radius=R, resolution=(30, 30))
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(sphere)

        # Create a cap
        cap_height = ValueTracker(0.1)
        cap = always_redraw(lambda: self.get_spherical_cap(R, cap_height.get_value()))

        # Height line
        height_line = always_redraw(lambda: Line(
            start=sphere.get_bottom(),
            end=sphere.get_bottom() + cap_height.get_value() * UP,
            color=YELLOW
        ))

        # Volume formula
        volume_formula = always_redraw(lambda: MathTex(
            "V = \\frac{1}{3} \\pi ", "{h}", "^2", "(3R - ", "{h}", ")",
            substrings_to_isolate="h"
        ).set_color_by_tex("h", YELLOW).next_to(height_line, RIGHT))

        # Animate
        self.add(cap, height_line, volume_formula)
        self.play(cap_height.animate.set_value(h_max), run_time=4, rate_func=there_and_back)
        self.wait()

    def get_spherical_cap(self, R, h):
        # Function to create a spherical cap
        return ParametricSurface(
            lambda u, v: np.array([
                R * np.sin(u) * np.cos(v),
                R * np.sin(u) * np.sin(v),
                R * np.cos(u)
            ]),
            u_range=[np.arccos(1 - h/R), PI],
            v_range=[0, TAU],
            resolution=(20, 20)
        ).set_color(RED)
