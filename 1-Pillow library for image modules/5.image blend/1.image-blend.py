from PIL import Image

img1 = Image.open(r"1-Pillow folder/5.image blend/moon.jpg").convert('L')
img1.show()

# creating a image2 object and convert it to mode 'P'
img2 = Image.open(r"1-Pillow folder/5.image blend/galaxy.jpg").convert('L')
img2.show()

# alpha is 1.0, a copy of the second image is returned
img = Image.blend(img1, img2, 0.6)  # opacity of 2nd image

# to show specified image
img.save('1-Pillow folder/5.image blend/moon-galaxy.jpg')
img.show()
