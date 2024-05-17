from PIL import Image

original = Image.open("cat.png")
width, height = original.size

steg = Image.new("RGB", (width, height))
bits = [1, 0, 0, 1, 1]

for i in range(width):
    for j in range(height):

        idx = 0
        r, g, b, a = original.getpixel((i, j))

        if bits[idx] == 0:
            r &= 254
        else:
            r |= 1

        steg.putpixel((i, j), (r, g, b, a))

        if idx < len(bits):
            idx += 1
        else:
            continue
steg.save("cat_withmessage.png")
