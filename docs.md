# PixelPalette Documentation

Welcome to the PixelPalette documentation! This guide will help you get started with PixelPalette, a Python library designed to simplify the creation and manipulation of pixel art images.

## Table of Contents

1. [Installation](#installation)
2. [Getting Started](#getting-started)
3. [Creating and Manipulating Images](#creating-and-manipulating-images)
4. [Drawing Shapes](#drawing-shapes)
5. [Applying Filters and Effects](#applying-filters-and-effects)
6. [Creating Animations](#creating-animations)
7. [Contributing](#contributing)
8. [License](#license)

## Installation

To install PixelPalette, use the following command:

```bash
pip install pixel-palett
from pixel_palette import PixelArt, draw_line, draw_rectangle, draw_circle

# Create a new 100x100 pixel image
art = PixelArt(100, 100)

# Draw a red line
draw_line(art.image, (10, 10), (90, 90), (255, 0, 0), width=2)

# Draw a blue rectangle
draw_rectangle(art.image, (20, 20), (80, 80), outline=(0, 0, 255), fill=(0, 0, 255))

# Draw a green circle
draw_circle(art.image, (50, 50), 30, outline=(0, 255, 0), fill=(0, 255, 0))

# Save the image
art.save('output.png')

from pixel_palette import PixelArt

# Create a new 100x100 pixel image
art = PixelArt(100, 100)
# Save the image
art.save('output.png')

# Load an image
art.load('input.png')

# Draw a single pixel
art.draw_pixel(50, 50, (255, 0, 0))

from pixel_palette import draw_rectangle

# Draw a blue rectangle
draw_rectangle(art.image, (20, 20), (80, 80), outline=(0, 0, 255), fill=(0, 0, 255))

from pixel_palette import draw_circle

# Draw a green circle
draw_circle(art.image, (50, 50), 30, outline=(0, 255, 0), fill=(0, 255, 0))

from pixel_palette import apply_blur

# Apply blur to the image
blurred_image = apply_blur(art.image, radius=2)

from pixel_palette import apply_sepia

# Apply sepia to the image
sepia_image = apply_sepia(art.image)

from pixel_palette import create_animation

# Create a list of frames
frames = [art.image for _ in range(5)]

# Create an animation
create_animation(frames, 'animation.gif', duration=500)
from pixel_palette import create_animation

# Create a list of frames
frames = [art.image for _ in range(5)]

# Create an animation
create_animation(frames, 'animation.gif', duration=500)

