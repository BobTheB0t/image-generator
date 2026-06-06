import argparse
from PIL import Image, ImageDraw, ImageFont

def generate_image(text, output_path, font_path='arial.ttf', font_size=40, image_size=(800, 600), background_color=(255, 255, 255), text_color=(0, 0, 0)):
    """
    Generate an image with the given text using Pillow.

    :param text: The text to be displayed on the image.
    :param output_path: The path where the generated image will be saved.
    :param font_path: The path to the font file. Defaults to 'arial.ttf'.
    :param font_size: The size of the font. Defaults to 40.
    :param image_size: The size of the image (width, height). Defaults to (800, 600).
    :param background_color: The background color of the image in RGB. Defaults to white.
    :param text_color: The color of the text in RGB. Defaults to black.
    """
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
        draw.text((x, y), text, fill=text_color, font=font)

        # Save the image to the specified output path
        image.save(output_path)
        print(f"Image generated successfully and saved to {output_path}")

    except FileNotFoundError:
        print(f"Error: Font file not found at {font_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate an image with text using Pillow.")
    parser.add_argument("text", type=str, help="The text to be displayed on the image.")
    parser.add_argument("output_path", type=str, help="The path where the generated image will be saved.")
    parser.add_argument("--font_path", type=str, default="arial.ttf", help="The path to the font file.")
    parser.add_argument("--font_size", type=int, default=40, help="The size of the font.")
    parser.add_argument("--image_size", type=lambda s: tuple(map(int, s.split(','))), default="800,600", help="The size of the image (width,height).")
    parser.add_argument("--background_color", type=lambda s: tuple(map(int, s.split(','))), default="255,255,255", help="The background color of the image in RGB.")
    parser.add_argument("--text_color", type=lambda s: tuple(map(int, s.split(','))), default="0,0,0", help="The color of the text in RGB.")

    args = parser.parse_args()

    generate_image(
        text=args.text,
        output_path=args.output_path,
        font_path=args.font_path,
        font_size=args.font_size,
        image_size=args.image_size,
        background_color=args.background_color,
        text_color=args.text_color
    )