import core.wahrol as wahrol
from PIL import Image
import gui.app as app
import utils.timetracker as tt

if __name__ == "__main__":
    app.Window("Wahrolator", (800, 600))
    perf, img = tt.get_performance(wahrol.wahrolate, Image.open('resources/andy.jpg'))
    img.save("resources/test.png")
    print(perf)
