from manim import *
from manim_slides import Slide

from util import text, coordinates

class Position(Slide):
    def __init__(self):
        super().__init__()
        self.title = "Positioning"


    def construct(self, render):
        render.add(NumberPlane())

        rectangle = Rectangle(color=RED, width=2, height=3).move_to(3*LEFT + UP)
        render.add(rectangle)
    
        render.wait()