from PIL import Image, ImageDraw, ImageFont
import textwrap


def generate_image_with_text(
    text, output_path, font_path="arial.ttf", font_size=40, image_size=(800, 600)
):
    """
    Generate an image with centered text using Pillow.

    :param text: The text to be written on the image.
    :param output_path: The path where the generated image will be saved.
    :param font_path: The path to the font file. Defaults to 'arial.ttf'.
    :param font_size: The size of the font. Defaults to 40.
    :param image_size: The size of the image. Defaults to (800, 600).
    """
    try:
        # Create a new image with a white background
        image = Image.new("RGB", image_size, color="white")
        draw = ImageDraw.Draw(image)

        # Load the font
        font = ImageFont.truetype(font_path, font_size)

        # Wrap the text to fit within the image width
        lines = textwrap.wrap(text, width=40)

        # Calculate the total height of the text block
        total_height = 0
        for line in lines:
            _, _, line_width, line_height = draw.textbbox((0, 0), line, font=font)
            total_height += line_height

        # Calculate the starting y position to center the text vertically
        y_position = (image_size[1] - total_height) // 2

        # Draw each line of text
        for line in lines:
            _, _, line_width, _ = draw.textbbox((0, 0), line, font=font)
            # Calculate the x position to center the text horizontally
            x_position = (image_size[0] - line_width) // 2
            draw.text((x_position, y_position), line, font=font, fill="black")
            y_position += font_size

        # Save the image
        image.save(output_path)
        print(f"Image saved to {output_path}")

    except FileNotFoundError:
        print(f"Font file not found at {font_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Example usage
    generate_image_with_text(
        "Hello, World!\nThis is a test image generated using Pillow.",
        "output_image.png",
    )