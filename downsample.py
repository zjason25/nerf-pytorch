from PIL import Image
import os

# downsamples the image by a factor

def downsample_images(input_folder):
    # Create the output folder 'image_8' if it doesn't exist
    output_folder = r'C:\Users\zhiji\nerf-pytorch\data\nerf_custom\figure_106\images_8'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    files = os.listdir(input_folder)
    print(files)

    # Filter JPG files
    jpg_files = [file for file in files if file.lower().endswith('.jpg') or file.lower().endswith('.jpeg') or file.lower().endswith('.JPG') or file.lower().endswith('.JPEG')]
    print(len(jpg_files))
    for filename in jpg_files:
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        with Image.open(input_path) as img:
            # Get the original image size
            width, height = img.size

            # Calculate the new dimensions for downsampling by a factor of 8
            new_width = width // 8
            new_height = height // 8

            # Downsample the image
            downscaled_img = img.resize((new_width, new_height), Image.LANCZOS)

            # Save the downsampled image in 'image_8' folder
            downscaled_img.save(output_path)

input_folder_path = r'C:\Users\zhiji\nerf-pytorch\data\nerf_custom\figure_106\images'

downsample_images(input_folder_path)
