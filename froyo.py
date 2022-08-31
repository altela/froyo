import os
from rembg import remove
from PIL import Image

input_path = 'images/'
output_path = 'result/'
counter = 1

for images in os.listdir(input_path):
    input = Image.open(str(input_path+images))
    output = remove(input)
    # output.save(output_path)
    basewidth = 400
    wpercent = (basewidth/float(output.size[0]))
    hsize = int((float(output.size[1])*float(wpercent)))
    gbr = output.resize((basewidth,hsize), Image.ANTIALIAS)

    nama_baru = images.split(".", 1)[0]

    background = Image.open("twibbon.png")
    background.paste(gbr, ((background.width - gbr.width) // 2, (background.height - gbr.height) // 2))
    background.save(output_path + str(nama_baru) + ".png",optimize=True,quality=95)

    print(f"Gambar {counter} berhasil diproses")
    counter += 1