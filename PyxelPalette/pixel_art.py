from PIL import Image

class PixelArt:
    def __init__(self, width, height):
        self.image = Image.new('RGB', (width, height), 'white')

    def save(self, filename):
        self.image.save(filename)

    def load(self, filename):
        self.image = Image.open(filename)

    def draw_pixel(self, x, y, color):
        self.image.putpixel((x, y), color)
