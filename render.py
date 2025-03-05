#!/usr/bin/env python3
import sys
import os
import importlib.util
from typing import Type
from manim import Scene, config
from utils.scene_checker import check_scene

def load_scene_class(file_path: str, scene_name: str) -> Type[Scene]:
    """Charge une classe de scène depuis un fichier Python."""
    # Obtenir le nom du module à partir du chemin
    module_name = os.path.splitext(os.path.basename(file_path))[0]
    
    # Charger le module
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Impossible de charger le fichier {file_path}")
        
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    
    # Obtenir la classe de scène
    if not hasattr(module, scene_name):
        raise ValueError(f"La scène {scene_name} n'existe pas dans {file_path}")
    
    scene_class = getattr(module, scene_name)
    if not issubclass(scene_class, Scene):
        raise TypeError(f"{scene_name} n'est pas une sous-classe de Scene")
    
    return scene_class

def main():
    if len(sys.argv) < 3:
        print("Usage: python render.py <fichier_animation.py> <nom_scene> [options_manim]")
        sys.exit(1)
        
    file_path = sys.argv[1]
    scene_name = sys.argv[2]
    manim_args = sys.argv[3:]
    
    try:
        # Charger la scène
        scene_class = load_scene_class(file_path, scene_name)
        
        # Créer une instance de la scène pour la vérification
        scene = scene_class()
        
        # Exécuter les vérifications
        print(f"\n🔍 Vérification de la scène {scene_name}...")
        if not check_scene(scene):
            print("\n⚠️ Des erreurs ont été détectées. Voulez-vous continuer ? (o/N)")
            response = input().lower()
            if response != 'o':
                print("Rendu annulé.")
                sys.exit(1)
        
        # Construire la commande manim
        manim_command = f"manim {' '.join(manim_args)} {file_path} {scene_name}"
        
        # Lancer le rendu
        print("\n🎬 Lancement du rendu...")
        os.system(manim_command)
        
    except Exception as e:
        print(f"\n❌ Erreur: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 