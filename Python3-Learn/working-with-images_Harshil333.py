'''
// AUTHOR: Harshil Doshi
// Python3 Concept: Working with Images in Python
// GITHUB: https://github.com/Harshil333 
'''

# PIL is the Python Imaging Library which provides the python interpreter with image editing capabilities.
# We’ll be working with Pillow which is a user-friendly PIL fork.

# Installation: pip install Pillow

# We can perform various tasks on the image using Pillow such as:

# Retreiving size of the image:
from PIL import Image 

filename = "image.png"
with Image.open(filename) as image: 
    #Image.size gives a 2-tuple and the width, height can be obtained
	width, height = image.size 


# Rotating an image:
from PIL import Image 
 
#Relative Path 
img = Image.open("picture.jpg") 
#Angle given 
img = img.rotate(180) 
#Saved in the same relative location 
img.save("rotated_picture.jpg") 


#Cropping an image:
from PIL import Image 

#Relative Path 
img = Image.open("picture.jpg") 
width, height = img.size 

area = (0, 0, width/2, height/2) 
img = img.crop(area) 

#Saved in the same relative location 
img.save("cropped_picture.jpg")