from manim import *
from manim_slides import Slide

from util import text, coordinates

class Equations(Slide):
    def __init__(self):
        super().__init__()
        self.title = "Latex"


    def construct(self, render):
        equation = MathTex(
            r"\sum^n_{i=1} i",
            r"=",
            r"{",
            r"n(n+1)",
            r"\over",
            r"2",
            r"}", 
            font_size=112, 
            color=BLACK,
            # substrings_to_isolate=["n+1"]
        )
        render.add(equation)

        # equation.set_color_by_tex("n+1", RED)

        arranged = MathTex(
            r"2", 
            r"\cdot",
            r"\sum^n_{i=1} i",
            r"=",
            r"n(n+1)", 
            font_size=112, 
            color=BLACK
        )

        arranged[0].set_color(RED)
        
        render.wait()
        render.next_slide()

        render.play(TransformMatchingTex(equation, arranged))

        render.wait()