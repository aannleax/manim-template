from manim import *
from manim_slides import Slide

from util import text, coordinates

class Basic(Slide):
    def __init__(self):
        super().__init__()
        self.title = "Basic"


    def construct(self, render):
        my_text = text.tex(r"Some text with math: ${a \over b} = c$").next_to(coordinates.UPPER_LEFT)
        render.add(my_text)

        flowers = ImageMobject(
            "images/flowers.png"
        ).scale_to_fit_height(3).next_to(
            my_text, DOWN, aligned_edge=LEFT, buff=1.0
        ).shift(RIGHT)
        render.add(flowers)

        buildings= ImageMobject(
            "images/buildings.jpg"
        ).scale_to_fit_height(3).next_to(flowers, RIGHT).set_x(-flowers.get_x())
        render.add(buildings)
    
        render.wait()