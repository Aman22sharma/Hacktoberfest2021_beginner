import qrcode
data = input("enter the data you want to make a qrcode of ")
img = qrcode.make(data)
img.save("qrcode.png")