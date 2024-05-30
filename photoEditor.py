from PIL import Image, ImageEnhance, ImageFilter
import os

path = './photos'
pathOut = '/edited_photos'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    clean_name = os.path.splitext(filename[0])

    if img.mode == 'RGBA':
        img = img.convert('RGB')

    edit = img.filter(ImageFilter.SHARPEN).convert('L')

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')
