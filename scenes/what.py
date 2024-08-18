from manim import *
from manim_slides import Slide

from util import text, coordinates

class What(Slide):
    def __init__(self):
        super().__init__()
        self.title = "What is Manim?"


    def construct(self, render):
        channel = ImageMobject("images/channel.png").scale_to_fit_width(0.8 * render.camera.frame_width)
        render.add(channel)

        render.wait()