# Challenge:
# 12. Create an image from code (png file) Hint: use Pillow

from PIL import Image, ImageDraw, ImageFont

img1 = Image.new(mode="RGB", size=(400, 300), color=(234, 456, 56))
img1.save("viber1.jpg")
img2 = Image.open("viber2.jpg")

img1 = img1.resize((2400, 2400))
img2 = img2.resize((2400, 2400))
img1 = img1.convert('RGB')
img2 = img2.convert('RGB')

alpha = 0.5
img_bl = Image.blend(img1, img2, alpha)
img_bl.save('blended_image.jpg')

img_bl.show()

input_image = Image.open('blended_image.jpg')
draw = ImageDraw.Draw(img_bl)
text_position = (80, 80)
font = ImageFont.truetype(font='arial.ttf', size=150)
text = "This is the PILLOW task!"
draw.text(text_position, text, font=font)
img_bl.save('output_image.jpg')

# Close the image
img_bl.show()
img_bl.close()
