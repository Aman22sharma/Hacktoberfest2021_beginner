# AUTHOR: Prathmesh Patil
# Python3 Concept: Detecting Indian Number Plates using Deep Learning
# GITHUB: https://github.com/patrickn699

# Install the below libaries

#pip install INPR
#pip install torch==1.7.1+cpu torchvision==0.8.2+cpu torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
#pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cpu/torch1.7/index.html

# import the libraries

from INPR import inpr
import matplotlib.pyplot as plt
%matplotlib inline

#npx degit patrickn699/INPR/test_img -f

img = 'kia.jpg'

# checking the image.
im = plt.imread(img)
plt.figure(figsize=(15,15))
plt.imshow(im)

# passing the image to detect the plates
grap,op,img = inpr.detect_plates(img)

# viewing the detected plate inside the image
plt.figure(figsize=(10,10))
plt.imshow(grap)

# get the number plate
plt = inpr.fetch_details(op,img)

# print the number plate
print(plt)
