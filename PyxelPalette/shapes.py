# pixel_palette/shapes.py

from PIL import ImageDraw

def draw_line(image, start, end, color, width=1):
    """
   Draw a line on an image.

    :param image: Image object to draw on.
    :param start: Starting coordinates (x, y).
    :param end: End coordinates (x, y).
    :param color: Color of the line (RGB tuple).
    :param width: Line thickness.
    """
    draw = ImageDraw.Draw(image)
    draw.line([start, end], fill=color, width=width)

def draw_rectangle(image, top_left, bottom_right, outline=None, fill=None):
    """
   Draw a rectangle on an image.

    :param image: Image object to draw on.
    :param top_left: Coordinates of the top left corner (x, y).
    :param bottom_right: Coordinates of the bottom right corner (x, y).
    :param outline: Outline color (RGB tuple).
    :param fill: Fill color (RGB tuple).
    """
    draw = ImageDraw.Draw(image)
    draw.rectangle([top_left, bottom_right], outline=outline, fill=fill)

def draw_circle(image, center, radius, outline=None, fill=None):
    """
   Draw a circle on a picture.

    :param image: Image object to draw on.
    :param center: Coordinates of the center (x, y).
    :param radius: Radius of the circle.
    :param outline: Outline color (RGB tuple).
    :param fill: Fill color (RGB tuple).
    """
    draw = ImageDraw.Draw(image)
    top_left = (center[0] - radius, center[1] - radius)
    bottom_right = (center[0] + radius, center[1] + radius)
    draw.ellipse([top_left, bottom_right], outline=outline, fill=fill)
