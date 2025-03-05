from manim import *
import inspect
from typing import List, Tuple, Any

class SceneChecker:
    def __init__(self, scene: Scene):
        self.scene = scene
        self.warnings = []
        self.errors = []
        
    def check_mobject_visibility(self, mobject: Mobject) -> None:
        """Vérifie si un mobject est visible dans la scène."""
        frame = self.scene.camera.frame
        mobject_center = mobject.get_center()
        mobject_height = mobject.height
        mobject_width = mobject.width
        
        # Vérifier si le mobject est trop petit
        if mobject_height < 0.05 or mobject_width < 0.05:
            self.warnings.append(f"Le mobject {mobject} est très petit (h:{mobject_height:.2f}, w:{mobject_width:.2f})")
            
        # Vérifier si le mobject est hors champ
        frame_height = frame.height
        frame_width = frame.width
        frame_center = frame.get_center()
        
        if (abs(mobject_center[0] - frame_center[0]) > frame_width/2 or
            abs(mobject_center[1] - frame_center[1]) > frame_height/2):
            self.errors.append(f"Le mobject {mobject} est hors champ")
            
    def check_animations(self) -> None:
        """Vérifie les animations définies dans la scène."""
        construct_source = inspect.getsource(self.scene.construct)
        
        # Vérifier si wait() est utilisé après play()
        if "self.play(" in construct_source and "self.wait(" not in construct_source:
            self.warnings.append("Aucun wait() trouvé après les animations. Considérez ajouter des pauses.")
            
    def check_scene_duration(self) -> None:
        """Vérifie la durée approximative de la scène."""
        total_duration = 0
        for animation in self.scene.animations:
            total_duration += animation.run_time
            
        if total_duration < 1:
            self.warnings.append(f"La scène est très courte ({total_duration:.1f}s)")
        elif total_duration > 60:
            self.warnings.append(f"La scène est très longue ({total_duration:.1f}s)")
            
    def check_color_contrast(self, mobject: Mobject) -> None:
        """Vérifie le contraste des couleurs avec le fond."""
        if hasattr(mobject, 'color'):
            background = self.scene.camera.background_color
            if mobject.color == background:
                self.warnings.append(f"Le mobject {mobject} a la même couleur que le fond")
                
    def run_all_checks(self) -> Tuple[List[str], List[str]]:
        """Exécute toutes les vérifications disponibles."""
        # Vérifier tous les mobjects dans la scène
        for mobject in self.scene.mobjects:
            self.check_mobject_visibility(mobject)
            self.check_color_contrast(mobject)
            
        # Vérifier les animations
        self.check_animations()
        self.check_scene_duration()
        
        return self.warnings, self.errors
        
def check_scene(scene: Scene) -> bool:
    """
    Fonction utilitaire pour vérifier une scène.
    Retourne True si aucune erreur n'est trouvée, False sinon.
    """
    checker = SceneChecker(scene)
    warnings, errors = checker.run_all_checks()
    
    if warnings:
        print("\n⚠️ Avertissements:")
        for warning in warnings:
            print(f"  - {warning}")
            
    if errors:
        print("\n❌ Erreurs:")
        for error in errors:
            print(f"  - {error}")
            
    if not errors and not warnings:
        print("\n✅ Aucun problème détecté!")
        
    return len(errors) == 0 