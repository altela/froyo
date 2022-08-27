from PIL import Image

background = Image.open("twibbon.png")
foreground = Image.open("/Users/pramardhika/Desktop/hasil_foto/")

background.paste(foreground, (165, 50), foreground)
background.show()