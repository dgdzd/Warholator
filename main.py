import core.wahrol as wahrol
from PIL import Image
import gui.app as app

app.Window("Wahrolator", (800, 600))

img = wahrol.wahrolate(Image.open('resources/eggplant.jpg'))
img.save("resources/test.png")
