import random
import array

MAX_LEN = 12
choice = "y"
while choice != "n":
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    lowercase = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

    uppercase = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "M",
        "N",
        "O",
        "p",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    sympols = [
        "@",
        "#",
        "$",
        "%",
        "=",
        ":",
        "?",
        ".",
        "/",
        "|",
        "~",
        ">",
        "*",
        "(",
        ")",
        "<",
    ]

    charlist = numbers + uppercase + lowercase + sympols

    rand_digit = random.choice(numbers)
    rand_upper = random.choice(uppercase)
    rand_lower = random.choice(lowercase)
    rand_symbol = random.choice(sympols)

    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(charlist)

        temp_pass_list = array.array("u", temp_pass)
        random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
        password = password + x

    print("\nPassword generated: " + password + "\n")
    choice = input("Generate a new password(y/n): ")