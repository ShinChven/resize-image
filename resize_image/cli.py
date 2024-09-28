import os
import argparse
from PIL import Image, features

def resize_image(file_path, max_length, quality, target_file_type):
    try:
        with Image.open(file_path) as img:
            orig_width, orig_height = img.size

            if orig_width > orig_height:
                target_width = max_length
                target_height = int((max_length / orig_width) * orig_height)
                target_size = f'w{target_width}'
            else:
                target_height = max_length
                target_width = int((max_length / orig_height) * orig_width)
                target_size = f'h{target_height}'

            img_resized = img.resize((target_width, target_height), Image.LANCZOS)

            if target_file_type:
                new_file_type = target_file_type.lower()
            else:
                new_file_type = img.format.lower()

            new_filename = f"{os.path.splitext(file_path)[0]}_{target_size}.{new_file_type}"
            img_resized.save(new_filename, new_file_type.upper(), quality=quality)
            print(f"Resized image saved as {new_filename}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def process_directory(directory, max_length, quality, target_file_type):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file.lower().endswith(('jpg', 'jpeg', 'png', 'bmp', 'gif', 'webp')):
                resize_image(file_path, max_length, quality, target_file_type)

def cli():
    if not features.check('webp'):
        print("WebP support is not available.")
        return

    parser = argparse.ArgumentParser(description='Resize images to a target maximum length while maintaining aspect ratio.')
    parser.add_argument('path', help='File path to an image or a directory containing images.')
    parser.add_argument('max_length', type=int, help='Max length for resizing.')
    parser.add_argument('--quality', type=int, default=100, help='Set target image quality, default is 100%.')
    parser.add_argument('--filetype', type=str, default=None, help='Set target file type, default is the original type.')

    args = parser.parse_args()

    if os.path.isfile(args.path):
        resize_image(args.path, args.max_length, args.quality, args.filetype)
    elif os.path.isdir(args.path):
        process_directory(args.path, args.max_length, args.quality, args.filetype)
    else:
        print("Provided path is neither a file nor a directory.")
