// AUTHOR: Bonifasius Tarigan
// Python3 Concept: Area of circle
// GITHUB: https://github.com/bonifasiustrg


r=int(input("type what is the radius of the circle:"))
if r%7==0:
    Area=(22/7)*r**2
else:
    Area=3.14*r**2
print("So, area of a circle with radius", r, "is","{:1}".format(Area))
