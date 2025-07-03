import os
from PIL import Image

while True:
    try:
        divisor = int(input("Enter reduction factor (1–10): "))
        if 1 <= divisor <= 10:
            break
        else:
            print("Please enter a number between 1 and 10.")
    except ValueError:
        print("Invalid input. Please enter a whole number between 1 and 10.")

input_folder = 'images'
output_folder = 'output'
output_format = 'PNG' 
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    input_path = os.path.join(input_folder, filename)
    name, ext = os.path.splitext(filename)

    try:
        with Image.open(input_path) as img:
            new_width = max(1, img.width // divisor)
            new_height = max(1, img.height // divisor)
            resized_img = img.resize((new_width, new_height))
            output_path = os.path.join(output_folder, f"{name}.{output_format.lower()}")
            resized_img.save(output_path, output_format)
            print(f"✅ {filename} resized to {new_width}x{new_height} and saved as {output_path}")
    except Exception as e:
        print(f"❌ Error processing {filename}: {e}")

