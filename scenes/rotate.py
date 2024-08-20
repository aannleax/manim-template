from manim import *
from manim_slides import Slide

from util import text, coordinates

class Rotation(Slide):
    def __init__(self):
        super().__init__()
        self.title = "Rotate"


    def construct(self, render):
        triangle = Triangle(color=GREEN)
        render.add(triangle)

        render.wait()
        render.next_slide()

        # render.play(triangle.animate.rotate(PI))

        render.play(Rotate(triangle, angle=PI))

        render.wait()