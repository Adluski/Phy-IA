from manim import *

class SV(ThreeDScene):
    def construct(self):
        radius = 2  # Radius of the sphere
        height = 2 * radius  # Height is twice the radius

        # Function to calculate y (radius of the disk at height h)
        def y(h):
            return np.sqrt(radius**2 - (h - radius)**2)

        # Create a sphere
        sphere = Sphere(radius=radius, resolution=(101, 51))
        sphere.set_color(RED_E)

        # Add the sphere to the scene
        self.add(sphere)

        # Create disks
        disks = VGroup()
        for h in np.linspace(0, height, 50):
            disk_radius = y(h)
            disk = Circle(radius=disk_radius)
            disk.set_stroke(width=0)
            disk.set_fill(BLUE_E, opacity=0.5)
            disk.move_to(sphere.get_center() + UP * (h - radius))
            disks.add(disk)

        # Animate the construction of the sphere from the disks
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.play(Create(disks), run_time=5)
        self.wait(2)
