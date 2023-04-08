from PIL import Image
import os

# Set the directory containing the PNG images
png_directory = "images"

# Set the directory to save the JPEG images
jpeg_directory = "converted_images"

# Create the directory for the JPEG images, if it does not exist
if not os.path.exists(jpeg_directory):
    os.makedirs(jpeg_directory)

# Loop through all files in the PNG directory
for filename in os.listdir(png_directory):
    if filename.endswith(".png"):
        # Open the PNG file
        with Image.open(os.path.join(png_directory, filename)) as img:
            # Convert the image to RGB format and save as JPEG
            img.convert("RGB").save(os.path.join(jpeg_directory,
                                                 os.path.splitext(filename)[0] + ".jpg"))
