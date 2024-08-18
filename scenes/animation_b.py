from manim import *
from manim_slides import Slide

from util import text, coordinates

class Example(Slide):
    def __init__(self):
        super().__init__()
        self.title = "Example"


    def construct(self, render):
        my_text = text.tex("Test").next_to(coordinates.UPPER_LEFT)
        render.add(my_text)

        circle = Circle(radius=2, color=BLUE)
        render.add(circle)

        render.wait()