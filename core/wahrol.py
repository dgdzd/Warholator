from PIL import Image
import numpy as np
import random
import math

MODE_REPLACE = 0
MODE_ADD = 1

def wahrolate(img: Image.Image, columns: int = 3, rows: int = 3, strength: int = 128, colors: int = 3, mode: int = MODE_REPLACE) -> Image.Image:
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

    :param colors:
        Défini par défaut à 3. Le nombre de couleurs constituant une palette. Une palette correspond à un ensemble de couleurs à appliquer sur un fragment.
    """
    ratio = rows / columns
    if ratio < 1:  # S'il y a plus de colonnes que de lignes.
        new_img = Image.new('RGB', (img.size[0], int(img.size[1] * ratio)))
        frag_size = (img.size[0] / columns, img.size[1] / rows * ratio)
    else: # S'il y a plus de lignes que de colonnes.
        new_img = Image.new('RGB', (int(img.size[0] / ratio), img.size[1]))
        frag_size = (img.size[0] / columns / ratio, img.size[1] / rows)

    # frag correspond à un "fragment" de l'image finale. Ce "fragment" est l'image redimensionnée en fonction du nombre de colonnes et de lignes voulu.
    frag = img.resize((math.ceil(frag_size[0]), math.ceil(frag_size[1]))).convert("RGB") 

    # On génère des palettes de n couleurs aléatoirement (colonnes * lignes) fois
    strength = max(0, min(255, strength)) # on recadre strength entre 0 et 255
    colors = [[[random.randint(-strength, strength) for i in range(3)] for j in range(colors)] for k in range(columns * rows)]

    for y in range(rows):
        for x in range(columns):
            # On colle une instance de frag filtrée par la fonction dépendant du mode choisi à la colonne et à la ligne correspondante.
            palette = colors[columns * y + x]
            top_left = (int(x * frag_size[0]), int(y * frag_size[1]))
            if mode == MODE_REPLACE:
                new_img.paste(_filter_replace(frag, palette), top_left)
            elif mode == MODE_ADD:
                new_img.paste(_filter_add(frag, palette), top_left)

    return new_img

def _filter_replace(img: Image.Image, colors: list[list[int]]):
    size = img.size
    pixels = np.array(img) # on prend chaque pixel dans un nparray pour optimiser le temps de traitement.
    for y in range(size[0]):
        for x in range(size[1]):
            col = pixels[x, y]
            gray = (int(col[0]) + int(col[1]) + int(col[2]))/3 # Le niveau de gris de l'image, qui servira à choisir la couleur à utiliser.
            pixels[x, y] = colors[int(gray // (256 / len(colors)))]

    return Image.fromarray(pixels)

def _filter_add(img: Image.Image, colors: list[list[int]]):
    size = img.size
    pixels = np.array(img) # on prend chaque pixel dans un nparray pour optimiser le temps de traitement.
    for y in range(size[0]):
        for x in range(size[1]):
            col = pixels[x, y]
            gray = (int(col[0]) + int(col[1]) + int(col[2]))/3 # Le niveau de gris de l'image, qui servira à choisir la couleur à utiliser.
            pixels[x, y] = _rebound(col, colors[int(gray // (256 / len(colors)))]) # On applique une fonction d'addition spéciale, Puis on change la couleur du pixel.

    return Image.fromarray(pixels)

def _rebound(c1: list[np.uint8], c2: list[int]):
    res = []
    for i in range(3):
        a = int(c1[i]) + c2[i] # ici c1[i] n'est pas un int, mais un uint8. On le convertit donc en int pour éviter les erreurs.
        if a > 255:
            res.append(255 + (255 - a))
        elif a < 0:
            res.append(-a)
        else:
            res.append(a)
    return res