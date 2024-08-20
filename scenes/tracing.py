
from manim import *
from manim_slides import Slide

from util import text, coordinates

class Tracing(Slide):
    def __init__(self):
        super().__init__()
        self.title = "Following"


    def construct(self, render):
        circle = Circle(color=BLUE).move_to(3*LEFT+2*UP)
        rect = Rectangle(color=RED).move_to(2*DOWN)

        render.add(circle)
        render.add(rect)

        arrow = always_redraw(
            lambda: Line(circle.get_bottom(), rect.get_top(), color=BLUE).add_tip(ArrowTriangleTip())
        )
        render.add(arrow)
        
        render.play(circle.animate.shift(6*RIGHT), run_time=2.0)

        render.wait()