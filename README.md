# Projet Manim

Ce projet contient des animations créées avec Manim.

## Installation

1. Créez un environnement virtuel Python :
```bash
python -m venv venv
source venv/bin/activate  # Sur Unix/MacOS
# ou
.\venv\Scripts\activate  # Sur Windows
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Structure du projet

- `config.py` : Configurations globales (couleurs, styles, etc.)
- `animations/` : Dossier contenant les fichiers d'animation
- `media/videos/` : Dossier où seront stockées les vidéos finales

## Utilisation

Pour rendre une animation sans les fichiers intermédiaires :

```bash
manim -qh animations/example.py ExampleScene
```

Options utilisées :
- `-q` : Qualité moyenne (utilisez `-qh` pour haute qualité, `-ql` pour basse qualité)
- `-p` : Pour prévisualiser la vidéo après le rendu

Les vidéos finales seront sauvegardées dans le dossier `media/videos/`. 