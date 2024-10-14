from PIL import Image
from PIL import ImageDraw
import numpy as np
import random

def wahrolate(img: Image.Image, iterations: int = 3) -> Image.Image:
    """
    La fonction principale du programme. Elle génère une image modifiée basée sur celle donnée.

    :param img: 
        L'image à modifier.

    :param iterations:
        Optionnel. Le nombre de divisions à faire.
    """
    new_img = Image.new('RGB', img.size)
    frag_size = (img.size[0] / iterations, img.size[1] / iterations)
    frag = img.resize((int(frag_size[0]), int(frag_size[1])))
    colors = [[(random.randint(-128, 128)) % 255 for i in range(3)] for j in range(9)]

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
            pixels[y, x] = [(col[i] + color[i])%255 for i in range(len(color))].append(col[3]) if img.mode == "RGBA" else [(col[i] + color[i])%255 for i in range(len(color))]

    return Image.fromarray(pixels)