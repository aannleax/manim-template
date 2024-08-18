from manim import *
from manim_slides import Slide

class Example(Slide):
    def __init__(self):
        super().__init__()
        self.title = "Example"


    def construct(self, render):
        circle = Circle(radius=2, color=BLUE)
        render.add(circle)

        render.wait()