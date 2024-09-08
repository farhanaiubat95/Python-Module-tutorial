from PIL import Image, ImageFilter

img = Image.open(
    "1-Pillow library for image modules/6.Image Filter/flower.jpg")
img.show()

# img.filter(ImageFilter.BLUR).show()
# img.filter(ImageFilter.MinFilter).show()  # same as MinFilter(3)
# img.filter(ImageFilter.CONTOUR).show()
# img.filter(ImageFilter.DETAIL).show()
# img.filter(ImageFilter.EDGE_ENHANCE).show()
# img.filter(ImageFilter.EDGE_ENHANCE_MORE).show()
# img.filter(ImageFilter.EMBOSS).show()
# img.filter(ImageFilter.FIND_EDGES).show()
# img.filter(ImageFilter.SHARPEN).show()
# img.filter(ImageFilter.SMOOTH).show()
img.filter(ImageFilter.SMOOTH_MORE).show()
