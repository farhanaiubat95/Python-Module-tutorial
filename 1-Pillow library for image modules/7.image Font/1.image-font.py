from PIL import Image, ImageDraw, ImageFont

img = Image.open("1-Pillow library for image modules/7.image Font/flower.jpg")

# object of Imagedraw class
draw = ImageDraw.Draw(img)

# object of ImageFont class
fontt = ImageFont.truetype("arial.ttf", 150)

# distance(x,y)
distance = 140, img.height/2

# text for writing over image
text = "This is a beautiful rose."

# call text() method by draw object
draw.text(distance, text, "white", font=fontt)

# display final look
img.show()
