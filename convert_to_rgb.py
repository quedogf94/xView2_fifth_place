from PIL import Image

def convert_to_rgb(image_path):
    image = Image.open(image_path)
    if image.mode == 'RGBA':
        image = image.convert('RGB')
        image.save(image_path)
        print(f"Converted {image_path} to RGB")
    else:
        print(f"{image_path} is already in RGB format")

paths = [
    'path_to_pre_image/1.png',
    'path_to_post_image/2.png'
]

for path in paths:
    convert_to_rgb(path)
