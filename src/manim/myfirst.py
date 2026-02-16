from manim import *

class MyFirstVideo(Scene):
    def construct(self):
        s1 = Square()

        self.play(Create(s1))
        for _ in range(100):
            self.play(Rotate(s1, 180*DEGREES, rate_func=linear))
            