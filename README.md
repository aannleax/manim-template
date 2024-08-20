# Manim Template

This is a template for presentations in [Manim](https://www.manim.community/) roughly following the [TU Dresden Slide template](https://tu-dresden.de/ing/informatik/smt/cgv/studium/materialien?set_language=en).

## Installation

1. Install dependencies for Manim as described here: https://docs.manim.community/en/stable/installation.html
2. Install [Manim-Slides](https://www.manim.community/plugin/manim-slides/) using
```
  pip install manim-slides[manim]
```

## Useful Links

Reference with animations: https://docs.manim.community/en/stable/reference_index/animations.html
Try Manim online: https://try.manim.community/

## Commands

Compiling and showing slides
```
manim slides.py Slides
manim-slides Slides
```

Setup command
```
manim-slides wizard
```

Convert to other formats:
```
manim-slides convert Slides --to=pdf
manim-slides convert Slides --to=html
```

