from PIL import Image

img = Image.open(
    "1-Pillow library for image modules/1.image open-rotate-show/elon musk.jpg")
img.show()  # image show
img_rotate = img.rotate(45)
img_rotate.show()  # rotate 45

# image size print
print(img.height)
print(img.width)
print(img.size)
print(img.format)
