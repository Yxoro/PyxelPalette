# pixel_palette/animations.py

from PIL import Image
import os

def create_animation(frames, output_path, duration=500):
    """
  Creates a GIF animation from a list of images.

    :param frames: List of Image objects representing the animation frames.
    :param output_path: Path to save the GIF animation.
    """
    if not frames:
        raise ValueError()

    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=0
    )

def save_animation(frames, output_path, duration=500):
    """
  Records a GIF animation from a list of images.

    :param frames: List of image paths representing the animation frames.
    :param output_path: Path to save the GIF animation.
    :param duration: Duration of each frame in milliseconds.
    """
    images = [Image.open(frame) for frame in frames]
    create_animation(images, output_path, duration)
