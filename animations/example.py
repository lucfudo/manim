from manim import *
import os
import sys

# Ajout du répertoire parent au path Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import *

class ExampleScene(Scene):
    def construct(self):
        # Création d'un titre
        title = create_title("Exemple d'Animation")
        
        # Création d'un cercle stylisé
        circle = styled_shape(Circle(radius=2))
        
        # Animation
        self.play(Write(title))
        self.wait()
        self.play(title.animate.to_edge(UP))
        self.play(Create(circle))
        self.wait()
        self.play(
            circle.animate.scale(0.5).set_fill(COLORS['secondary']),
            run_time=ANIMATION_TIMES['normal']
        )
        self.wait() 