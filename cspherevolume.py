from manim import *

class SphericalCapVolumeProof(Scene):
    def construct(self):
        # Introduce the sphere and spherical cap
        sphere_radius = 3
        cap_height = 2
        cap_radius = self.calculate_cap_radius(sphere_radius, cap_height)

        # Texts for introduction
        intro_texts = [
            Tex("Consider a sphere of radius $R$"),
            Tex("and a spherical cap with height $h$"),
            Tex("We want to prove the volume of the spherical cap is"),
            Tex("$V = \\frac{1}{3} \\pi h^2 (3R - h)$"),
        ]

        # Display introduction texts
        for text in intro_texts:
            self.play(Write(text))
            self.wait(1)
            self.play(FadeOut(text))

        # Show the relation V_cap = V_cyl - V_cone
        relation_text = Tex(
            "$V_{\\text{cap}} = V_{\\text{cyl}} - V_{\\text{cone}}$"
        ).shift(UP * 3)

        self.play(Write(relation_text))

        # Representations of the cylinder and cone
        cylinder = Cylinder(radius=cap_radius, height=cap_height)
        cone = Cone(radius=cap_radius, height=cap_height)

        # Display cylinder and cone
        self.play(FadeIn(cylinder))
        self.wait(1)
        self.play(Transform(cylinder, cone))
        self.wait(1)

        # Show the actual formula derivation
        derivation_text = MathTex(
            "V_{\\text{cyl}}", "=", "\\pi", "a^2", "h",
            "\\quad\\text{and}\\quad",
            "V_{\\text{cone}}", "=", "\\frac{1}{3}", "\\pi", "a^2", "h"
        ).shift(UP * 2)

        self.play(Write(derivation_text))
        self.wait(2)

        # Show the radius of the cap base (a) in terms of sphere's radius (R) and cap's height (h)
        a_formula = MathTex(
            "a", "=", "\\sqrt{h(2R-h)}"
        ).next_to(derivation_text, DOWN)

        self.play(Write(a_formula))
        self.wait(2)

        # Combine everything to show the final formula
        final_formula = MathTex(
            "V_{\\text{cap}}", "=", "\\pi a^2 h - \\frac{1}{3} \\pi a^2 h",
            "=", "\\frac{2}{3} \\pi a^2 h"
        ).next_to(a_formula, DOWN)

        self.play(Write(final_formula))
        self.wait(2)

        # Replace a^2 with h(2R-h)
        final_formula_with_a_substituted = MathTex(
            "V_{\\text{cap}}", "=", "\\frac{2}{3} \\pi", "h(2R-h)", "h",
            "=", "\\frac{1}{3} \\pi h^2 (3R - h)"
        ).next_to(final_formula, DOWN)

        self.play(Transform(final_formula, final_formula_with_a_substituted))
        self.wait(2)

        # Conclude
        conclude_text = Tex("Hence proved!").shift(DOWN * 3)
        self.play(Write(conclude_text))
        self.wait(2)

    def calculate_cap_radius(self, sphere_radius, cap_height):
        return (cap_height * (2 * sphere_radius - cap_height))**0.5


