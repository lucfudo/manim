from manim import *

# Couleurs personnalisées
COLORS = {
    'primary': "#2D5BA3",
    'secondary': "#A32D2D",
    'highlight': "#FFD700",
    'background': "#1A1A1A",
}

# Configuration des styles de texte
TEXT_CONFIG = {
    'font_size': 36,
    'color': WHITE,
}

# Configuration des formes
SHAPE_CONFIG = {
    'stroke_width': 2,
    'fill_opacity': 0.8,
}

# Durées d'animation par défaut
ANIMATION_TIMES = {
    'fast': 0.5,
    'normal': 1.0,
    'slow': 2.0,
}

# Fonction utilitaire pour créer un titre stylisé
def create_title(text, scale_factor=1.0):
    return Text(
        text,
        font_size=TEXT_CONFIG['font_size'] * scale_factor,
        color=TEXT_CONFIG['color']
    )

# Fonction utilitaire pour créer un groupe de formes avec style cohérent
def styled_shape(shape, color=COLORS['primary']):
    return shape.set_style(
        stroke_width=SHAPE_CONFIG['stroke_width'],
        fill_opacity=SHAPE_CONFIG['fill_opacity'],
        fill_color=color
    ) 