# AUTHOR: Surya Wiguna
# Python3 Concept: Discount calculator
# GITHUB: https://github.com/suryawiguna

#discount calculator code
print("<----Count your final price after discount---->")

# formation of the function
def getFinalPrice(percentage, sub_total):
    final_price = (sub_total - ((sub_total * percentage) / 100))
    return final_price

sub_total = float(input("Total spending you did: "))

percentage = float(input("Total discount on the spending: "))

print("Your grandtotal after the discount is: ", getFinalPrice(percentage, sub_total))
