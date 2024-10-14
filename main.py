import core.wahrol as wahrol
from PIL import Image

img = wahrol.wahrolate(Image.open('resources/eggplant.jpg'))
img.save("resources/test.png")
img.show()