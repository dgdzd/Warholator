from PIL import Image
from PIL import ImageDraw
import numpy as np
import random
import math

def wahrolate(img: Image.Image, iterations: int = 3, seed: int = -1) -> Image.Image:
    """
    La fonction principale du programme. Elle génère une image modifiée basée sur celle donnée.

    :param img: 
        L'image à modifier.

    :param iterations:
        Optionnel. Le nombre de divisions à faire.

    :param seed:
        Optionnel. Définit les filtres de couleur de chaque division de l'image
    """
    comp_count = 4 if img.mode == "RGBA" else 3
    new_img = Image.new('RGB', img.size)
    frag_size = (img.size[0] / iterations, img.size[1] / iterations)
    frag = img.resize((int(frag_size[0]), int(frag_size[1])))
    if seed == -1:
        seed = random.randint(-512, 512)
    colors = [[(random.randint(-128, 128)) % 255 for i in range(comp_count)] for j in range(9)]

    for x in range(iterations):
        for y in range(iterations):
            frag = _filter(frag, colors[iterations * x + y])
            new_img.paste(frag, (int(x * frag_size[0]), int(y * frag_size[1])))

    return new_img

def _filter(img: Image.Image, color: list[int]):
    size = img.size
    pixels = np.array(img)
    for x in range(size[0]):
        for y in range(size[1]):
            col = pixels[y, x]
            pixels[y, x] = [(col[i] + color[i])%255 for i in range(len(color))]

    return Image.fromarray(pixels)