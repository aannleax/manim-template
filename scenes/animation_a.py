from manim import *
from manim_slides import Slide

from util import text, coordinates

class AnimationA(Slide):
    def __init__(self):
        super().__init__()
        self.title = "Example (1)"
        self.triangle_color = BLUE

    def construct(self, render):
        du = 0.2 * DOWN
        d1 = Dot(LEFT*4+du)
        d2 = Dot(RIGHT*2+du)
        d3 = Dot(RIGHT*1+UP*3+du)
      
        triangle = Polygon(
            d1.get_center(),d2.get_center(),d3.get_center(),
            color = self.triangle_color,
            stroke_width = 8
        )
        render.add(triangle)
        
        alpha_arc = Angle.from_three_points(d2,d1,d3, color=self.triangle_color)
        beta_arc = Angle.from_three_points(d3,d2,d1, color=self.triangle_color)
        gamma_arc = Angle.from_three_points(d1,d3,d2, color=self.triangle_color)
        
        render.add(alpha_arc)
        render.add(beta_arc)
        render.add(gamma_arc)
        
        alpha = text.math(r"\alpha").next_to(d1).shift(0.3*RIGHT+0.2*UP)
        beta = text.math(r"\beta").next_to(d2, UP).shift(0.4*LEFT)
        gamma = text.math(r"\gamma").next_to(d3, DOWN).shift(0.2*DOWN+0.2*LEFT)
        angles = VGroup(alpha, beta, gamma)

        render.add(alpha)
        render.add(beta)
        render.add(gamma)
        
        render.wait()
        render.next_slide()

        equation_1 = text.math(r"\alpha").move_to(2 * DOWN)
        equation_2 = text.math(r"\alpha", " + ", r"\beta").move_to(2 * DOWN)
        equation_3 = text.math(r"\alpha", " + ", r"\beta", " + ", r"\gamma").move_to(2 * DOWN)
        equation_4 = text.math(r"\alpha", " + ", r"\beta", " + ", r"\gamma", r" = 180^\circ").move_to(2 * DOWN)
        
        render.play(TransformMatchingTex(alpha.copy(), equation_1))
        render.wait()
        render.play(TransformMatchingTex(Group(equation_1, beta.copy()), equation_2))
        render.wait()
        render.play(TransformMatchingTex(Group(equation_2, gamma.copy()), equation_3))        
        render.wait()
        render.play(TransformMatchingTex(equation_3, equation_4))        

        render.wait()
