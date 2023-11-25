from manim import *

class SphericalCapVolume(Scene):
    def construct(self):
        # Parameters for the sphere and cap
        sphere_radius = 2
        cap_height = ValueTracker(1)

        # Sphere and cap
        sphere = Sphere(radius=sphere_radius, resolution=(101, 51)).set_opacity(0.5)
        cap = always_redraw(lambda: 
            Hemisphere(radius=sphere_radius, resolution=(101, 51))
            .set_height(cap_height.get_value(), stretch=True)
            .move_to(sphere.get_top(), DOWN)
            .set_color(BLUE)
        )

        # Volume formula text
        volume_formula = always_redraw(lambda: 
            MathTex("V = \\frac{\\pi h^2 (3R - h)}{3}", "=", 
                f"{PI * cap_height.get_value()**2 * (3 * sphere_radius - cap_height.get_value()) / 3:.2f}")
            .to_edge(UP)
        )

        # Height value updater
        height_label = always_redraw(lambda: 
            MathTex("h =", f"{cap_height.get_value():.2f}")
            .next_to(cap, UP)
        )

        # Animation
        self.play(Create(sphere))
        self.play(Write(volume_formula), GrowFromCenter(cap))
        self.add(height_label)
        self.wait(1)
        self.play(cap_height.animate.set_value(sphere_radius), rate_func=there_and_back, run_time=4)
        self.wait(1)
