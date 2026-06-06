import os
from PIL import Image, ImageDraw, ImageFont

def generate_image(text, output_path, font_path='arial.ttf', font_size=40, image_size=(800, 600), background_color=(255, 255, 255), text_color=(0, 0, 0)):
    """
    Generate an image with the given text using Pillow.

    Args:
        text (str): The text to be displayed on the image.
        output_path (str): The path where the generated image will be saved.
        font_path (str, optional): The path to the font file. Defaults to 'arial.ttf'.
        font_size (int, optional): The size of the font. Defaults to 40.
        image_size (tuple, optional): The size of the image (width, height). Defaults to (800, 600).
        background_color (tuple, optional): The background color of the image in RGB. Defaults to (255, 255, 255) (white).
        text_color (tuple, optional): The color of the text in RGB. Defaults to (0, 0, 0) (black).

    Raises:
        FileNotFoundError: If the font file is not found.
        ValueError: If the text is empty.
    """

    # Check if the text is empty
    if not text.strip():
        raise ValueError("Text cannot be empty")

    # Check if the font file exists
    if not os.path.isfile(font_path):
        raise FileNotFoundError(f"Font file not found at {font_path}")

    try:
        # Create a new image with the specified size and background color
        image = Image.new('RGB', image_size, background_color)
        draw = ImageDraw.Draw(image)

        # Load the font
        font = ImageFont.truetype(font_path, font_size)

        # Calculate the text size and position it in the center of the image
        text_width, text_height = draw.textsize(text, font=font)
        x = (image_size[0] - text_width) / 2
        y = (image_size[1] - text_height) / 2

        # Draw the text on the image
        draw.text((x, y), text, font=font, fill=text_color)

        # Save the image to the specified output path
        image.save(output_path)
        print(f"Image generated successfully at {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate an image with text using Pillow.")
    parser.add_argument("text", type=str, help="The text to be displayed on the image")
    parser.add_argument("output_path", type=str, help="The path where the generated image will be saved")
    parser.add_argument("--font_path", type=str, default="arial.ttf", help="The path to the font file")
    parser.add_argument("--font_size", type=int, default=40, help="The size of the font")
    parser.add_argument("--image_width", type=int, default=800, help="The width of the image")
    parser.add_argument("--image_height", type=int, default=600, help="The height of the image")
    parser.add_argument("--background_color", type=str, default="255,255,255", help="The background color of the image in RGB (e.g., 255,255,255)")
    parser.add_argument("--text_color", type=str, default="0,0,0", help="The color of the text in RGB (e.g., 0,0,0)")

    args = parser.parse_args()

    # Convert color arguments from strings to tuples
    background_color = tuple(map(int, args.background_color.split(',')))
    text_color = tuple(map(int, args.text_color.split(',')))

    generate_image(
        args.text,
        args.output_path,
        font_path=args.font_path,
        font_size=args.font_size,
        image_size=(args.image_width, args.image_height),
        background_color=background_color,
        text_color=text_color
    )