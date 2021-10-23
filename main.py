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
'''

MODE = "GUI"
IMAGE = "resources/andy.jpg"
COLONNES = 3
LIGNES = 3
FORCE = 128

if __name__ == "__main__":

    if MODE == "DEMO":
        perf, img = performance.get_performance(wahrol.wahrolate, Image.open(IMAGE), COLONNES, LIGNES, FORCE)
        print(f"La fonction wahrolate() s'est exécutée en {perf.get_execution_time()}s")
        img.save(f"out/test.png")
        img.show()

    elif MODE == "GUI":
        app.Window("Wahrolator", (800, 600))
