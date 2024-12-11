from PIL import Image, ImageDraw, ImageFont

def create_meme(image_path, top_text, bottom_text, output_path, font_path="arial.ttf", font_size=40, resize_width=None):
    # Open the image
    img = Image.open(image_path)

    # Resize image if requested
    if resize_width:
        aspect_ratio = img.height / img.width
        new_height = int(resize_width * aspect_ratio)
        img = img.resize((resize_width, new_height), Image.ANTIALIAS)

    draw = ImageDraw.Draw(img)
    width, height = img.size

    # Load the custom font
    try:
        font = ImageFont.truetype(font_path, size=font_size)
    except IOError:
        print("Defaulting to a basic font. Install a TTF font for better styling.")
        font = ImageFont.load_default()

    # Define text position and styling
    margin = 10

    # Add top text
    if top_text:
        top_text_size = draw.textsize(top_text, font=font)
        top_position = ((width - top_text_size[0]) // 2, margin)
        draw.text(top_position, top_text, fill="white", font=font, stroke_fill="black", stroke_width=2)

    # Add bottom text
    if bottom_text:
        bottom_text_size = draw.textsize(bottom_text, font=font)
        bottom_position = ((width - bottom_text_size[0]) // 2, height - bottom_text_size[1] - margin)
        draw.text(bottom_position, bottom_text, fill="white", font=font, stroke_fill="black", stroke_width=2)

    # Save the result
    img.save(output_path)
    print(f"Meme saved at {output_path}")

# Example usage
if __name__ == "__main__":
    # Get user inputs
    image_path = input("Enter the path to the image: ")
    top_text = input("Enter the top text (leave blank for none): ")
    bottom_text = input("Enter the bottom text (leave blank for none): ")
    output_path = input("Enter the output path (e.g., output.jpg): ")

    # Optional customization
    font_path = input("Enter the font path (leave blank for default Arial): ") or "arial.ttf"
    font_size = int(input("Enter the font size (default 40): ") or 40)
    resize_width = input("Enter the resize width (leave blank for no resizing): ")
    resize_width = int(resize_width) if resize_width else None

    # Generate the meme
    create_meme(image_path, top_text, bottom_text, output_path, font_path, font_size, resize_width)
