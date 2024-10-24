import core.wahrol as wahrol
from PIL import Image
import gui.app as app
import utils.performance as performance

'''
Modifiez les différentes variables pour obtenir des résultats différents.

MODE: Définis le mode d'exécution. 
    - Mettre "DEMO" pour tester uniquement la fonction de génération d'image.
    - Mettre "GUI" pour tester l'interface

IMAGE: Le chemin de l'image à traiter.

COLONNES: Le nombre de divisions de l'image sur l'axe des abcisses.

LIGNES: Le nombre de divisions de l'image sur l'axe des ordonnées.

FORCE: L'écart des valeurs de couleurs possible entre celles de l'image de base et celles des résultats.
       Des valeurs plus proches de 0 donneront des résultats assez homogène, tandis que des valeurs plus 
       proche de 255 donneront des résultats plus chaotiques.

COULEURS: Le nombre de couleurs constituant une palette. Une palette correspond à l'ensemble des couleurs 
appliquées sur une division de l'image.

FILTRE: Le mode de l'algorithme. 
- Le mode MODE_ADD prend la couleur initiale de l'image et applique une fonction d'addition spéciale avec 
les couleurs de la palette.
- Le mode MODE_REPLACE ne prend en compte que les couleurs de la palette et ne prend que la couleur initiale
de l'image pour définir le niveau de gris.
'''

MODE = "DEMO"
IMAGE: str = "resources/andy.jpg"
COLONNES: int = 3
LIGNES: int = 3
FORCE: int = 256
COULEURS: int = 3
FILTRE: int = wahrol.MODE_REPLACE

if __name__ == "__main__":

    if MODE == "DEMO":
        perf, img = performance.get_performance(wahrol.wahrolate, Image.open(IMAGE), COLONNES, LIGNES, FORCE, COULEURS, FILTRE)
        print(f"La fonction wahrolate() s'est exécutée en {perf.get_execution_time()}s")
        file = IMAGE.split("/")[-1].split("\\")[-1].split(".") # On récupère le nom et l'extension du fichier
        img.save(f"out/{file[0]}-{COLONNES}x{LIGNES}_{COULEURS}_{FILTRE}.png")
        img.show()

    elif MODE == "GUI":
        app.Window("Wahrolator", (800, 600))
