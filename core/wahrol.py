from PIL import Image
import numpy as np
import random
import math

def wahrolate(img: Image.Image, columns: int = 3, rows: int = 3, strength: int = 128) -> Image.Image:
    """
    La fonction principale du programme. Elle génère une image modifiée basée sur celle donnée.

    :param img: 
        L'image à modifier.

    :param columns:
        Défini par défaut à 3. Le nombre de divisions à faire sur l'axe des abscisses.

    :param rows:
        Défini par défaut à 3. Le nombre de divisions à faire sur l'axe des ordonnées.

    :param strength:
        Défini par défaut à 128. L'écart des valeurs de couleurs possible entre celles de l'image de base et celles des résultats.
        Des valeurs plus proches de 0 donneront des résultats assez homogène, tandis que des valeurs plus proche de 255 donneront
        des résultats plus chaotiques.
    """
    ratio = rows / columns
    if ratio < 1:  # S'il y a plus de colonnes que de lignes
        new_img = Image.new('RGB', (img.size[0], int(img.size[1] * ratio)))
        frag_size = (img.size[0] / columns, img.size[1] / rows * ratio)
    else: # S'il y a plus de lignes que de colonnes
        new_img = Image.new('RGB', (int(img.size[0] / ratio), img.size[1]))
        frag_size = (img.size[0] / columns / ratio, img.size[1] / rows)

    # frag correspond à un "fragment" de l'image finale. Ce "fragment" est l'image redimensionnée en fonction du nombre de colonnes et de lignes voulu.
    frag = img.resize((math.ceil(frag_size[0]), math.ceil(frag_size[1]))).convert("RGB") 

    # On génère les couleurs aléatoirement
    strength = max(0, min(255, strength)) # on recadre strength entre 0 et 255
    colors = [[random.randint(-strength, strength) for i in range(3)] for j in range(columns * rows)]

    for y in range(rows):
        for x in range(columns):
            # On colle une instance de frag filtrée par la fonction _filter() à la colonne et à la ligne correspondante.
            new_img.paste(_filter(frag, colors[columns * y + x]), (int(x * frag_size[0]), int(y * frag_size[1])))

    return new_img

def _filter(img: Image.Image, color: list[int]):
    size = img.size
    pixels = np.array(img) # on prend chaque pixel dans un nparray pour optimiser le temps de traitement.
    for y in range(size[0]):
        for x in range(size[1]):
            col = pixels[x, y]
            final_color = _rebound(col, color) # On applique une fonction d'addition spéciale.
            pixels[x, y] = final_color

    return Image.fromarray(pixels)

def _rebound(c1: list[int], c2: list[int]):
    res = []
    for i in range(3):
        a = int(c1[i]) + c2[i]
        if a > 255:
            res.append(255 + (255 - a))
        elif a < 0:
            res.append(-a)
        else:
            res.append(a)
    return res