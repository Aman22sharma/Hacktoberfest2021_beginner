# AUTHOR: Surya Wiguna
# Python3 Concept: Discount calculator
# GITHUB: https://github.com/suryawiguna

#discount calculator code
print("Count your final price after discount")

def getFinalPrice(percentage, sub_total):
    final_price = (sub_total + ((sub_total * percentage) / 100))
    return final_price

sub_total = int(input("How much is the price?"))

percentage = float(input("How much is the discount?"))

print (getFinalPrice(percentage, sub_total))