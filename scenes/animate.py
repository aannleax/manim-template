from manim import *
from manim_slides import Slide

from util import text, coordinates

class Animate(Slide):
    def __init__(self):
        super().__init__()
        self.title = "Animate"


    def construct(self, render):
        circle = Circle(fill_color=RED, fill_opacity=1.0).move_to(4*LEFT)
        triangle = Triangle(color=GREEN)
        rectangle = Rectangle(width=2.0, height=2.0, color=BLUE).move_to(4*RIGHT)

        render.add(circle, triangle, rectangle)

        render.wait()
        render.next_slide()

        render.play(circle.animate.set_fill(BLUE))
        render.play(triangle.animate.shift(2*UP), run_time=2.0)
        render.play(rectangle.animate.scale(1.5))

        render.wait()