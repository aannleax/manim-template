from manim import *
from manim_slides import Slide

from util import text, coordinates

class Community(Slide):
    def __init__(self):
        super().__init__()
        self.title = "The Manim Community"


    def construct(self, render):
        exposition = ImageMobject(
            "images/announcement.png"
        ).scale_to_fit_width(
            0.4 * render.camera.frame_width
        ).next_to(ORIGIN, LEFT)
        
        participants = ImageMobject(
            "images/summer_videos.jpg"
        ).scale_to_fit_width(
            0.4 * render.camera.frame_width
        ).next_to(ORIGIN, RIGHT)

        render.add(exposition)
        render.add(participants)

        render.wait()