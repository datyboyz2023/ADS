from PIL import Image
import os

image_path = r"C:\Users\Admin\Downloads\img1.webp"
base_save_path = "F:\ADS\Practicals\Practicals\Practical-07"

if not os.path.exists(base_save_path):
    os.makedirs(base_save_path)

original_img = Image.open(image_path)

resize_img = original_img.copy()
resize_size = (300, 300)
resize_img = resize_img.resize(resize_size)
resize_save_path = os.path.join(base_save_path, 'resized_Raiden.jpg')
resize_img.save(resize_save_path)
print(f"Resized image saved at: {resize_save_path}")

grayscale_img = original_img.copy()
grayscale_img = grayscale_img.convert("L")
grayscale_save_path = os.path.join(base_save_path, 'grayscale_Raiden.jpg')
grayscale_img.save(grayscale_save_path)
print(f"Grayscale image saved at: {grayscale_save_path}")

thumbnail_img = original_img.copy()
max_size = (128, 128)
thumbnail_img.thumbnail(max_size)
thumbnail_save_path = os.path.join(base_save_path, 'thumbnail_Raiden.jpg')
thumbnail_img.save(thumbnail_save_path)
print(f"Thumbnail image saved at: {thumbnail_save_path}")
