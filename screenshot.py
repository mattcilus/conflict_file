from PIL import Image # Notice the 'from PIL' at the start of the line

im = Image.new("RGB", (200, 30), "#ddd")
im.save("C:\\Users\\Duc\\Downloads\\image.png")
