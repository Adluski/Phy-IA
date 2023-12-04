from manim import *

class LineOfLengthE(Scene):
    def construct(self):
        # Define a line of length e
        line = Line(start=ORIGIN, end=RIGHT * np.e, stroke_width=2)

        # Create a label for the line
        label = MathTex("e").next_to(line, DOWN)

        # Drawing the line and the label
        self.play(Create(line))
        self.play(Write(label))

        # Hold the scene
        self.wait(2)
