import os
from PIL import Image, ImageEnhance

# Define the input and output folder
input_path = 'result/'
output_path = 'result/'

# Brightness factor (e.g., 1.2 for 20% brighter)
brightness_factor = 1.2

# Ensure the output folder exists
os.makedirs(output_path, exist_ok=True)

# Process each image in the input folder
for filename in os.listdir(input_path):
    # Create the full path to the image
    img_path = os.path.join(input_path, filename)
    
    # Check if it's a file and has a valid image extension
    if os.path.isfile(img_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        # Open the image
        img = Image.open(img_path)

        # Enhance the brightness
        enhancer = ImageEnhance.Brightness(img)
        img_enhanced = enhancer.enhance(brightness_factor)

        # Save the enhanced image
        save_path = os.path.join(output_path, filename)
        img_enhanced.save(save_path)

        print(f"Processed and saved: {save_path}")
