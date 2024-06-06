from manim import *

class SquareToCircle(Scene):
    def construct(self):
        title_text = Text("Data Visualization", font="Arial", font_size=45, color=WHITE)
        author_text = Text("By Rodney and Brendon", font="Arial", font_size=45, color=WHITE)
        title_text.next_to(author_text, UP)

        self.play(Write(title_text))
        self.wait(0.5)
        self.play(Write(author_text))
        self.wait(2)
        self.play(FadeOut(title_text), FadeOut(author_text))
        self.wait(1)
