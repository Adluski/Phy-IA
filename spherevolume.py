from manim import *

class SV(ThreeDScene):
    def construct(self):
        # Define the radius of the sphere
        radius = 2

        # Create a sphere
        sphere = Sphere(radius=radius, resolution=(101, 51))
        sphere.set_color(BLUE_E)
        sphere.set_opacity(0.5)

        # Create a cube with side length 2r (same as sphere diameter)
        cube = Cube(side_length=2 * radius)
        cube.set_color(RED_E)
        cube.set_opacity(0.5)
        cube.move_to(sphere.get_center())

        # Position the sphere and cube side by side
        group = Group(sphere, cube)
        group.arrange(RIGHT, buff=1)

        # Add the objects to the scene
        self.add(group)

        # Rotate the group to show 3D perspective
        self.move_camera(phi=45 * DEGREES, theta=45 * DEGREES)
        self.wait(2)

        # Rotate the objects for better view
        self.play(Rotate(group, angle=PI, axis=UP))
        self.wait(2)
