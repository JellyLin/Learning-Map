import Image
import os
import sys

def crop(infile,height,width):
	im = Image.open(infile)
	imgwidth, imgheight = im.size
	for i in range(imgheight//height):
		for j in range(imgwidth//width):
			box = (j*width, i*height, (j+1)*width, (i+1)*height)
			yield im.crop(box)
# 2048

# 32 * 64
# 16 * 128
# 8  * 256
# 4  * 512
# 2  * 1024
# 1  * 2048
if __name__ == "__main__":
    if len(sys.argv) > 1:
        size = sys.argv[1]
    else:
		size = 1

size = int(size)
infile="Resize-2048x2048.jpg"
zoom = pow(2,size-1)
height= 2048/zoom
width=height
start_num=0
for k,piece in enumerate(crop(infile,height,width),start_num):
	img=Image.new('RGB', (height,width), 255)
	img.paste(piece)
	path=("temp/" + str(size-1)+"/" + str(k/zoom) + "/"+ str(k%zoom) +".jpg")
	print str(path)
	img.save(path)
	img = Image.open(path)
	img_resize = img.resize((256, 256), Image.NEAREST) # use nearest neighbour
	img_resize.save(path)