import os
from rembg import remove
from PIL import Image
from pillow_heif import register_heif_opener

input_path = 'result/'
output_path = 'result/'

for image_file in os.listdir(input_path):
    if image_file.endswith(".png"):
        image_path = os.path.join(input_path, image_file)
        image_name, _ = os.path.splitext(image_file)
        output_file = os.path.join(output_path, image_name + ".jpg")

        try:
            img = Image.open(image_path).convert("RGBA")

            # Create a new white background image with the same size as the PNG image
            background_color = (255, 255, 255, 255)  # White color with full opacity
            new_img = Image.new("RGBA", img.size, background_color)

            # Paste the PNG image onto the white background, preserving transparency
            new_img.paste(img, (0, 0), img)

            # Convert the image to RGB mode before saving as JPEG
            new_img_rgb = new_img.convert("RGB")

            # Save the resulting image with transparency preserved as JPEG
            new_img_rgb.save(output_file, "JPEG", quality=95)
            print(f"Converted {image_file} to {image_name}.jpg")

            # Remove the original PNG file after converting to JPEG
            os.remove(image_path)
            print(f"Removed {image_file} after conversion.")
        except Exception as e:
            print(f"Failed to convert {image_file}: {e}")
