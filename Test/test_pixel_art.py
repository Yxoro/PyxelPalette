import unittest
from PyxelPalette import PixelArt

class TestPixelArt(unittest.TestCase):
    def test_create_image(self):
        art = PixelArt(10, 10)
        self.assertEqual(art.image.size, (10, 10))

    def test_draw_pixel(self):
        art = PixelArt(10, 10)
        art.draw_pixel(5, 5, (255, 0, 0))
        self.assertEqual(art.image.getpixel((5, 5)), (255, 0, 0))

if __name__ == '__main__':
    unittest.main()
