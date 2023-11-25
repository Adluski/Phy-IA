from manim import *

class S(ThreeDScene):
    def construct(self):
        # Parameters for the sphere
        sphere_radius = 2
        sphere = Sphere(radius=sphere_radius, resolution=(50, 50)).set_opacity(0.5)
        
        # The radius line from the center of the sphere to the surface
        radius_line = Line(ORIGIN, sphere_radius * UP, color=WHITE)

        # Text for the radius 'R'
        radius_text = Text('R', font_size=24).next_to(radius_line, RIGHT, buff=0.1)
        
        # The height of the spherical cup
        cup_height = 0.5
        height_line = Line(
            sphere_radius * DOWN + cup_height * UP,
            sphere_radius * DOWN, color=WHITE
        ).add_tip()
        
        # Text for the height 'h'
        height_text = Text('h', font_size=24).next_to(height_line, RIGHT, buff=0.1)

        # Arc to represent the cup
        arc = Arc(
            start_angle=PI, angle=-PI, radius=sphere_radius - cup_height,
            color=RED
        ).shift(cup_height * DOWN)

        # Add the elements to the scene
        self.add(sphere)
        self.add(radius_line)
        self.add(radius_text)
        self.add(height_line)
        self.add(height_text)
        self.add(arc)
        
        # Camera settings
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

scene = SphericalCupIllustration()
scene.render()
