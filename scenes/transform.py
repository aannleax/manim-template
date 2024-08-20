from manim import *
from manim_slides import Slide

from util import text, coordinates

class TransformObjects(Slide):
    def __init__(self):
        super().__init__()
        self.title = "Transform"


    def construct(self, render):
        circle = Circle(radius=2, fill_color=BLUE, fill_opacity=1.0).move_to(3*LEFT)
        render.add(circle)

        render.wait()
        render.next_slide()

        rectangle = Rectangle(fill_color=RED, fill_opacity=1.0).move_to(3*RIGHT)
        render.play(TransformFromCopy(circle, rectangle))
    
        render.next_slide()
        rectangle.shift(DOWN)
        circle.shift(LEFT)

        render.wait()
        render.next_slide()

        group = VGroup(circle, rectangle)
        triangle = Triangle()
        render.play(Transform(group, triangle))

        render.wait()