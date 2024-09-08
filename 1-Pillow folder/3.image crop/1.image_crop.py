from PIL import Image

img = Image.open("1-Pillow folder/3.image crop/Sadman.jpg")
img.show()
print("First image size : ", img.size)

area = (200, 60, 650, 700)  # (x1,y1,x2,y2)
image_crop = img.crop(area)
image_crop.save('1-Pillow folder/3.image crop/Croped image.jpg')
print("After cropping : ", image_crop.size)
image_crop.show()
