
def checker1(password):
    global specialcharacter
    specialcharacter=False

    for i in password:
        if i=="@" or i=="!" or i=="#" or i=="$" or i=="%" or i=="^" or i=="&" or i=="*" or i=="(" or i==")":
            specialcharacter=True

    return specialcharacter


def checker2(password):
    global numeric
    numeric=False
    for i in password:

        if i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9" or i=="0":
            numeric=True

    return numeric
def checker3(password):
    global capital
    capital=False
    for i in password:
        if i.isupper():
            capital=True

    return capital
def lengher(password):
    global length
    a=len(str(password))
    if a<8:
        length = False
    else:
        length =True
    return length

if __name__ == '__main__':
    password = input("Enter Password:")

    checker1(password)
    checker2(password)
    checker3(password)
    lengher(password)
    import time
    print("Calculating password:")
    time.sleep(0.5)

    if capital==True and numeric==True and specialcharacter==True and length==True:
        time.sleep(1)
        print("Password is Strong.")
        print("Length of password <8 : ", length)
        time.sleep(0.5)

        print("Capital Letter: ", capital)
        time.sleep(0.5)

        print("Numeric Letter: ", numeric)
        time.sleep(0.5)

        print("Special Letter: ", specialcharacter)
        time.sleep(0.5)
    else:
        time.sleep(0.5)
        print("Password is week.")

        time.sleep(0.5)

        print("Length of password <8 : ",length)
        time.sleep(0.5)

        print("Capital Letter: ", capital)
        time.sleep(0.5)

        print("Numeric Letter: ", numeric)
        time.sleep(0.5)

        print("Special Letter: ", specialcharacter)
        time.sleep(0.5)

        print("Please Add the letters which are false above.")






