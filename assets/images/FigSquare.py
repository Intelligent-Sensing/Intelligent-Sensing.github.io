from PIL import Image
import os

def crop_to_square(image_path, output_path):
    img = Image.open(image_path)
    width, height = img.size
    size = min(width, height)
    left = (width - size) // 2
    top = (height - size) // 2
    right = left + size
    bottom = top + size
    cropped_img = img.crop((left, top, right, bottom))
    cropped_img.save(output_path)

def main(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp','.jfif')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            crop_to_square(input_path, output_path)
            print(f"Cropped {filename} to square and saved to {output_path}")

if __name__ == "__main__":
    input_directory = "./headshots_original/"  # Replace with your input directory
    output_directory = "./"  # Replace with your output directory
    main(input_directory, output_directory)