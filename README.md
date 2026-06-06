# Image Generator

A simple Python script to generate images with text using the Pillow library.

## Prerequisites

- Python 3.7 or higher
- Pillow library (`pip install pillow`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/image-generator.git
   cd image-generator
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script with the following command:
```bash
python generate_image.py --text "Your Text Here" --output output_image.png
```

### Command-line Arguments

- `--text`: The text to be displayed on the image (required).
- `--output`: The output image file name (default: `output.png`).
- `--font`: The font file to use (default: `arial.ttf`).
- `--font-size`: The font size (default: `40`).
- `--image-size`: The image size in `widthxheight` format (default: `800x600`).
- `--background-color`: The background color in RGB format (default: `white`).
- `--text-color`: The text color in RGB format (default: `black`).

Example:
```bash
python generate_image.py --text "Hello, World!" --output hello.png --font-size 60 --image-size 1000x800 --background-color 255,255,255 --text-color 0,0,0
```

## Code Overview

The script consists of a single file `generate_image.py` with the following functions:

- `parse_arguments()`: Parses command-line arguments using `argparse`.
- `load_font(font_path, font_size)`: Loads the specified font with the given size.
- `create_image(width, height, background_color)`: Creates a new image with the specified size and background color.
- `add_text(image, text, font, text_color, position)`: Adds text to the image at the specified position.
- `save_image(image, output_path)`: Saves the image to the specified file path.
- `main()`: The main function that orchestrates the image generation process.

### Error Handling

The script includes error handling for:

- Missing or invalid command-line arguments.
- Font file not found.
- Invalid color format.
- Invalid image size format.

## Example

Here's an example of generating an image with the text "Hello, World!":

```bash
python generate_image.py --text "Hello, World!" --output hello.png
```

This will create an image file `hello.png` with the text "Hello, World!" in the center.

## Contributing

Feel free to submit pull requests or open issues for any bugs or feature requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Requirements

```python
# requirements.txt
Pillow>=9.0.0
```

## Script Code

```python
# generate_image.py
import argparse
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import os

def parse_arguments():
    """
    Parses command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Generate an image with text.")
    parser.add_argument("--text", required=True, help="The text to display on the image.")
    parser.add_argument("--output", default="output.png", help="The output image file name.")
    parser.add_argument("--font", default="arial.ttf", help="The font file to use.")
    parser.add_argument("--font-size", type=int, default=40, help="The font size.")
    parser.add_argument("--image-size", default="800x600", help="The image size in widthxheight format.")
    parser.add_argument("--background-color", default="255,255,255", help="The background color in RGB format.")
    parser.add_argument("--text-color", default="0,0,0", help="The text color in RGB format.")
    return parser.parse_args()

def load_font(font_path, font_size):
    """
    Loads the specified font with the given size.
    """
    try:
        return ImageFont.truetype(font_path, font_size)
    except IOError:
        raise ValueError(f"Font file not found: {font_path}")

def create_image(width, height, background_color):
    """
    Creates a new image with the specified size and background color.
    """
    try:
        rgb = tuple(map(int, background_color.split(',')))
        if len(rgb) != 3 or any(val < 0 or val > 255 for val in rgb):
            raise ValueError("Invalid background color format. Use RGB format (e.g., 255,255,255).")
        return Image.new("RGB", (width, height), rgb)
    except ValueError as e:
        raise ValueError(f"Invalid background color: {e}")

def add_text(image, text, font, text_color, position):
    """
    Adds text to the image at the specified position.
    """
    try:
        rgb = tuple(map(int, text_color.split(',')))
        if len(rgb) != 3 or any(val < 0 or val > 255 for val in rgb):
            raise ValueError("Invalid text color format. Use RGB format (e.g., 0,0,0).")
        draw = ImageDraw.Draw(image)
        draw.text(position, text, font=font, fill=rgb)
    except ValueError as e:
        raise ValueError(f"Invalid text color: {e}")

def save_image(image, output_path):
    """
    Saves the image to the specified file path.
    """
    image.save(output_path)

def main():
    args = parse_arguments()

    try:
        width, height = map(int, args.image_size.split('x'))
    except ValueError:
        raise ValueError("Invalid image size format. Use widthxheight format (e.g., 800x600).")

    image = create_image(width, height, args.background_color)
    font = load_font(args.font, args.font_size)

    # Calculate text position (center of the image)
    text_width, text_height = font.getsize(args.text)
    position = ((width - text_width) // 2, (height - text_height) // 2)

    add_text(image, args.text, font, args.text_color, position)
    save_image(image, args.output)

    print(f"Image saved to {args.output}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
```

Note: The above script code is also included in the `generate_image.py` file in the repository. The `requirements.txt` file is also included in the repository.