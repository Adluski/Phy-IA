from manim import *

class SphericalCapVolume(ThreeDScene):
    def construct(self):
        # Parameters for the sphere and spherical cap
        R = 3  # Radius of the sphere
        h = 1  # Height of the spherical cap
        a = (R**2 - (R - h)**2)**0.5  # Radius of the base of the spherical cap
        
        # Create the full sphere with radius R
        sphere = Sphere(radius=R).set_opacity(0.5).set_color(BLUE)

        # Create the spherical cap by slicing the sphere in half
        cap = Sphere(radius=R).set_opacity(0.5).set_color(RED)
        cap_mesh = SurfaceMesh(cap)
        cap_mesh.set_stroke(width=0.5).set_color(RED)
        
        # Function to remove the bottom half of the sphere's points
        def remove_bottom_half(points):
            for point in points:
                if point[2] < 0:  # If the z-coordinate is below 0
                    point[2] = 0  # Set z-coordinate to 0 (slice the sphere)
            return points
        
        # Apply the function to the sphere mesh to create a hemisphere
        cap_points = cap_mesh.get_all_points()
        new_points = remove_bottom_half(cap_points)
        cap_mesh.set_points(new_points)

        # Position the hemisphere correctly as a cap
        cap.shift(UP*h)

        # Display the text and formulas
        volume_text = MathTex(r"V = \frac{1}{3}\pi h^2 (3R - h)").to_corner(UL)
        volume_formula_crater = MathTex(r"V = \frac{1}{6}\pi h (3a^2 + h^2)").next_to(volume_text, DOWN)

        # Animate the creation and transformation of the sphere and cap
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.add(sphere)
        self.play(Create(cap_mesh))
        self.wait(2)

        # Show the volume formulas
        self.play(Write(volume_text), Write(volume_formula_crater))
        self.wait(2)

        # Animate the equivalence of the volumes
        self.play(Transform(cap_mesh, sphere))
        self.wait(2)

        # Clear the scene
        self.play(FadeOut(sphere), FadeOut(cap_mesh), FadeOut(volume_text), FadeOut(volume_formula_crater))
        self.wait(2)

# To run this scene, use the following command in your terminal:
# manim -pql vcap.py SphericalCapVolume
