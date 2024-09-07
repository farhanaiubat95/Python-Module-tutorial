from PIL import Image

size = height, width = (400, 450)
new_image1 = Image.new("RGB", size)  # new(mood,size,color)
new_image1.show()

new_image2 = Image.new("RGB", size, 'rgb(20%,40%,40%)')  # new(mood,size,color)
new_image2.show()
