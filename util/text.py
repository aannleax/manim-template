from manim import *

def tex(text, color = ManimColor(list([0.0, 0.1875, 0.3672])), font_size = 32):
    return Tex(text, color=color, tex_template=TexFontTemplates.helvetica_fourier_it, font_size=font_size)

def math(*text, color = ManimColor(list([0.0, 0.1875, 0.3672])), font_size = 32):
    return MathTex(*text, color=color, tex_template=TexFontTemplates.helvetica_fourier_it, font_size=font_size)