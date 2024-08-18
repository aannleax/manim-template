from manim import *
from manim_slides import Slide

from util import text, coordinates

from scenes import title, what, community, animation_a

create_title = False

# Put your slides here
slides = [
    # what.What(),
    # community.Community(),
    animation_a.AnimationA(),
]

title_long = "Creating Animated Slides With"
title_short = "Creating Slides With Manim"
authors_long = "Alex Ivliev"
authors_short = "Alex Ivliev"
affiliation = "Knowledge-Based Systems, TU Dresden"
date = "Retreat 2024, 21st of August"

class Slides(Slide):
    def draw_background(render, current, max):
        background = ImageMobject("images/background.png")
        background.scale_to_fit_height(render.camera.frame_height)
        background.scale_to_fit_width(render.camera.frame_width)
        render.add(background)

        coordinate_title = 4 * LEFT + 3.45 * DOWN
        coordinate_slide = 1.5 * RIGHT + 3.6 * DOWN
        coordinate_number = coordinate_slide + 1.0 * RIGHT

        title = text.tex(title_short, color = GRAY, font_size= 18).next_to(coordinate_title, RIGHT)
        author = text.tex(authors_short, color = GRAY, font_size= 18).next_to(coordinate_title, RIGHT).shift(0.25 * DOWN)
        render.add(title)
        render.add(author)

        slides_text = text.tex("Slide", color = GRAY, font_size= 18).next_to(coordinate_slide, RIGHT)
        slides_current = text.tex(f'{current}', color = GRAY, font_size= 18).next_to(coordinate_number, LEFT).align_to(coordinate_number, RIGHT)
        slides_max = text.tex(f'of {max}', color = GRAY, font_size= 18).next_to(coordinate_number, RIGHT, buff=0.1)
    
        render.add(slides_max)
        render.add(slides_current)
        render.add(slides_text)

    def draw_slide_title(render, title):
        text_title = text.tex(f'\\textbf{{{title}}}', color = GRAY, font_size=42).next_to(coordinates.UPPER_LEFT + 0.25 * UP, RIGHT, aligned_edge=DOWN)
        render.add(text_title)

    def construct(self):
        if create_title:
            title.Title(
                authors = authors_long, 
                title = title_long, 
                affiliation = affiliation, 
                date = date,
            ).construct(self)
            
        for (index, slide) in enumerate(slides):
            self.next_slide()

            self.clear()
            self.draw_background(index + 1, len(slides))
            self.draw_slide_title(slide.title)
          
            slide.construct(self)

        self.wait()