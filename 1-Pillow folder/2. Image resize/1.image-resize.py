from PIL import Image

img = Image.open("1-Pillow folder/2. Image resize/Ayman.jpg")
img.show()
print("First image size : ", img.size)

new_img_size = (400, 200)
img.thumbnail(new_img_size)
img.save('1-Pillow folder/2. Image resize/new_ayman.jpg')
print("New image size : ", img.size)
