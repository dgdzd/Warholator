import core.wahrol as wahrol
from PIL import Image
import gui.app as app
import utils.timetracker as tt
import random

if __name__ == "__main__":
    app.Window("Wahrolator", (800, 600))
    perf, img = tt.get_performance(wahrol.wahrolate, Image.open('resources/andy.jpg'))
    img.save(f"out/test-{random.randint(1000, 9999)}.png")
    print(perf)
