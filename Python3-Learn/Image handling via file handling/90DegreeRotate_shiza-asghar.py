#// AUTHOR: Shiza Asghar
#// Python3 Concept: (90 Degree Rotate)
#// GITHUB: shiza-asghar
'''
Given Lab03t.pgm is Text PGM file, has a text header
as described below and rest of the part is sequences
of bytes as binary for the shade of gray of specific pixel

Header
	P2 as fisrt two characters followed by a newline
	then two integers width and height of image in pixels
				seperated by a space followed by a newline
	then the total number of shades of gray followed by a newline
	and lastly the data in binary form of length width X height

'''

class TextPGM:
	pass

def ReadTextPGM(pgmFileName):

	img = TextPGM()

	f = open(pgmFileName)

	img.header = f.readline().rstrip()
	img.width, img.height = f.readline().rstrip().split(" ")
	img.shades = f.readline().rstrip()

	img.width = int(img.width)
	img.height = int(img.height)
	img.shades = int(img.shades)

	lines = f.readlines()

	f.close()

	img.data = []
	for line in lines:
		nums = line.rstrip().split(" ")
		for num in nums:
			img.data.append(int(num))

	return img

def WriteTextPGM(newpgmFileName, img):

	f = open(newpgmFileName, "w")

	f.write(img.header + "\n")
	f.write(str(img.width) + " " + str(img.height) + "\n")
	f.write(str(img.shades) + "\n")

	line = 0
	for num in img.data:
		f.write(str(num))
		line += 1
		if line % 10 == 0:
			f.write("\n")
		else:
			f.write(" ")

	f.close()

def main():
    img = ReadTextPGM("Lab03t1.pgm")
    print("Image properties")
    print("================")
    print("Signature", img.header)
    print("Width", img.width)
    print("Height", img.height)
    print("Shades", img.shades)
    print("Data Size from different ways")
    print(len(img.data))
    print(img.width*img.height)
    newImg = img
    for i in range(img.width*img.height):
        newImg.data[i] = int((img.data[i]-100) / 100 * 255)
        if newImg.data[i] < 0:
            newImg.data[i] = 0
        if newImg.data[i] > 255:
            newImg.data[i] = 255
    WriteTextPGM("Lab03t2.pgm",newImg)
	#rotating the image by 90 degree:
    #=================================
    invimage = TextPGM()
    invimage.width = img.height
    invimage.height = img.width
    invimage.shades = img.shades
    invimage.header = img.header
    invimage.data = []
    for i in range(img.width):
        k = 0
        for j in range(img.height):
            k = i+((img.width)*j)
            l = img.data[k]
            invimage.data.append(int(l))
    WriteTextPGM("inverted.pgm",invimage)
    return

main()
