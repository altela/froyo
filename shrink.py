import glob 
from PIL import Image

folder_gambar = glob.glob("/Users/pramardhika/Desktop/hasil_foto/*.jpg")
counter = 1
for gambar in folder_gambar:

	# with open(gambar, 'rb') as file:
	gbr = Image.open(gambar)

	basewidth = 400
	wpercent = (basewidth/float(gbr.size[0]))
	hsize = int((float(gbr.size[1])*float(wpercent)))
	gbr = gbr.resize((basewidth,hsize), Image.ANTIALIAS)

	gbr.save("/Users/pramardhika/Desktop/hasil_foto/"+str(counter)+".png",optimize=True,quality=95)
	counter += 1



	# counter = 1
	# basewidth = 400
	# wpercent = (basewidth/float(gambar.size[0]))
	# hsize = int((float(gambar.size[1])*float(wpercent)))
	# gambar = gambar.resize((basewidth,hsize), Image.ANTIALIAS)

	# gambar.save("/Users/pramardhika/Desktop/hasil_foto/hasil.png",optimize=True,quality=95)

	# counter += 1






# from PIL import Image

# basewidth = 400
# foo = Image.open("/Users/pramardhika/Desktop/hasil_foto/1659684676196.png")
# wpercent = (basewidth/float(foo.size[0]))
# hsize = int((float(foo.size[1])*float(wpercent)))
# foo = foo.resize((basewidth,hsize), Image.ANTIALIAS)

# foo.save("/Users/pramardhika/Desktop/hasil_foto/hasil.png",optimize=True,quality=95)