def seat_type(seat_number = int(input("Enter the seat number: "))):
    """
    input : - seat number (int)
    return : - seat type (string)
    Given a railway seat number, the task is to check whether it is a valid seat number or not.
    Also print its berth type i.e lower berth, middle berth, upper berth, side lower berth, side upper berth.
    """
    if seat_number>0 and seat_number<73:
        if seat_number % 8 == 1 or seat_number % 8 == 4:
            print(seat_number, " is lower berth")
        elif seat_number % 8 == 2 or seat_number % 8 == 5 :
            print(seat_number, " is middle berth")
        elif seat_number % 8 == 3 or seat_number % 8 == 6:
            print(seat_number, " is upper berth")
        elif seat_number % 8 == 7 :
            print(seat_number, " is side lower berth")
        else:
            print(seat_number," is side upper berth")

    else:
        print(seat_number," is invalid")

seat_type()