import sys
import os.path
from PIL import Image, ImageDraw, ImageFont
import numpy as np

def luminance_to_color(lum):
    """
    Convert luminance to one of 25 colors in a spectrum.
    """
    level = int((lum / 255) * 24)
    colors = [
        (0, 0, 128), (0, 0, 160), (0, 0, 192), (0, 0, 224), (0, 0, 255),
        (0, 128, 255), (0, 160, 255), (0, 192, 255), (0, 224, 255), (0, 255, 255),
        (0, 255, 224), (0, 255, 192), (0, 255, 160), (0, 255, 128), (0, 255, 0),
        (128, 255, 0), (160, 255, 0), (192, 255, 0), (224, 255, 0), (255, 255, 0),
        (255, 224, 0), (255, 192, 0), (255, 160, 0), (255, 128, 0), (255, 0, 0)
    ]
    return colors[level]

def draw_text_with_outline(draw, x, y, text, font):
    """
    Draw text with a white outline for better visibility.
    """
    # Draw black outline
    for dx, dy in [(-1,-1), (-1,1), (1,-1), (1,1), (-2,0), (2,0), (0,-2), (0,2)]:
        draw.text((x + dx, y + dy), text, (0, 0, 0), font=font)
    # Draw white text
    draw.text((x, y), text, (255, 255, 255), font=font)

def get_average_luminance(grayscale_array, x, y, radius=5):
    """
    Get average luminance in a region around a point.
    """
    height, width = grayscale_array.shape
    x1, x2 = max(0, x-radius), min(width, x+radius+1)
    y1, y2 = max(0, y-radius), min(height, y+radius+1)
    region = grayscale_array[y1:y2, x1:x2]
    return int(np.mean(region))

def create_luminance_map(image_path):
    with Image.open(image_path) as img:
        # Convert to RGB if not already
        img = img.convert('RGB')
        # Convert to grayscale for luminance values
        grayscale = img.convert("L")
        grayscale_array = np.array(grayscale)
        colorized_array = np.zeros((*grayscale_array.shape, 3), dtype=np.uint8)

        # Create colorized luminance map
        for i in range(grayscale_array.shape[0]):
            for j in range(grayscale_array.shape[1]):
                lum = grayscale_array[i, j]
                colorized_array[i, j] = luminance_to_color(lum)

        # Create scale bar
        scale_height = 50
        scale_bar = np.zeros((scale_height, colorized_array.shape[1], 3), dtype=np.uint8)

        for i, color in enumerate(luminance_to_color(i * 255 // 24) for i in range(25)):
            start_x = int(i * scale_bar.shape[1] / 25)
            end_x = int((i + 1) * scale_bar.shape[1] / 25)
            scale_bar[:, start_x:end_x] = color

        # Combine image and scale bar
        combined_image_array = np.vstack((colorized_array, scale_bar))
        combined_image = Image.fromarray(combined_image_array)

        # Add text annotations
        draw = ImageDraw.Draw(combined_image)
        
        # Use a larger font size
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
        except:
            font = ImageFont.load_default()

        # Draw scale bar values
        for i in range(25):
            lum_value = f"{int(i * 255 / 24)}-{int((i + 1) * 255 / 24 - 1)}"
            text_width = draw.textlength(lum_value, font=font)
            x = int((i + 0.5) * combined_image.width / 25 - text_width / 2)
            y = colorized_array.shape[0] + (scale_height - 24) // 2
            draw_text_with_outline(draw, x, y, lum_value, font)

        # Save the result
        dir_name, file_name = os.path.split(image_path)
        output_path = os.path.join(dir_name, "processed_" + file_name)
        combined_image.save(output_path)
        print(f"Processed image saved as: {output_path}")

def main():
    if len(sys.argv) > 1:
        for image_path in sys.argv[1:]:
            create_luminance_map(image_path)
    else:
        print("No image path provided.")

if __name__ == "__main__":
    main()
