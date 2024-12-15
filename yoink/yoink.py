from manim import * 

class Yoink(Scene):
    def construct(self):
        t= Text("Python animasjon er ganske vilt")

        self.play(Write(t))

        
