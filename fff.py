from PIL import Image


img = Image.new('RGB', (1200, 480), "white")

img1 = Image.open("Chart_1.png")
img2 = Image.open("Chart_2.png")

img_size = img1.resize((525, 360))
img1_size = img2.resize((525, 360))

img.paste(img1, (0, 0))
img.paste(img2, (580, 0))

img.show()
img.save("Chart_3.png")