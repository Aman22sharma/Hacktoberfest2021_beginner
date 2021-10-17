# AUTHOR: Neethu Joji George
# Python3 Concept: Tip Calculator Using Python
# GITHUB: https://github.com/NeethuJojiGeorge

#tip calculator code
print("Bill Calculator With the Tip")

def gettip(percentage, sub_total):
    tip = ((sub_total * percentage) / 100)
    total = (sub_total + tip)
    return total

sub_total = int(input("How much is the bill?"))

percentage = float(input("What percentage should the tip be?"))

print (gettip(percentage, sub_total))
