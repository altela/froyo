import os
from rembg import remove
from PIL import Image
from pillow_heif import register_heif_opener

input_path = 'images/'
output_path = 'result/'
counter = 1

for images in os.listdir(input_path):
    if images == ".DS_Store":
        try:
            os.remove(".DS_Store")
        except:
            pass
    else:
        check_extension = os.path.splitext(images)
        file_extension = check_extension[1]

        if file_extension == ".HEIC":
            register_heif_opener()
            input = Image.open(str(input_path+images))
        else:
            input = Image.open(str(input_path+images))
        output = remove(input)  

        basewidth = 400
        wpercent = (basewidth/float(output.size[0]))
        hsize = int((float(output.size[1])*float(wpercent)))
        new_size = output.resize((basewidth,hsize), Image.ANTIALIAS)

        new_name = images.split(".", 1)[0]

        # this will save image with no central watermark
        white_background = Image.open("white.png")
        white_background.paste(new_size, ((white_background.width - new_size.width) // 2, (white_background.height - new_size.height) // 2))
        white_background.save(output_path + str(new_name) + " no watermark.png",optimize=True,quality=95)

        # this will save image with watermark
        watermark = Image.open("watermark.png")
        watermark.paste(new_size, ((watermark.width - new_size.width) // 2, (watermark.height - new_size.height) // 2))
        watermark.save(output_path + str(new_name) + ".png",optimize=True,quality=95)

        print(f"Gambar {counter} berhasil diproses")
        counter += 1
