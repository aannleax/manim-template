from dataclasses import dataclass

from manim import *
from manim_slides import Slide

from util import text

@dataclass
class Title(Slide):
    title: str
    authors: str
    affiliation: str
    date: str

    def construct(self, render):
        background = ImageMobject("images/title.png")
        background.scale_to_fit_height(render.camera.frame_height)
        background.scale_to_fit_width(render.camera.frame_width)
        render.add(background)

        coordinate_start = 6 * LEFT + 1 * UP

        text_authors = text.tex(self.authors, color = WHITE, font_size=24).next_to(coordinate_start, RIGHT)
        text_affiliation = text.tex(self.affiliation, color = WHITE, font_size=24).next_to(text_authors, DOWN, buff=0.35).align_to(text_authors, LEFT)
        text_title = text.tex(f'\\textbf{{{self.title}}}', color = WHITE, font_size = 42).next_to(text_affiliation, DOWN, buff=0.35).align_to(text_authors, LEFT)
        text_date = text.tex(self.date, color = WHITE, font_size=24).shift(3 * DOWN).align_to(text_authors, LEFT)

        render.add(text_authors)
        render.add(text_affiliation)
        render.add(text_title)
        render.add(text_date)

        render.wait()

    
   
    
