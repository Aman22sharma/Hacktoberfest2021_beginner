#AUTHOR:  GOURAV CHAWLA 
#Python3 Concept: Simple ATM in Python
#GITHUB: https://github.com/gouravchawla334

while True:
    balance=10000;
    print("                         <<--        Welcome to ATM      -->>                         ")
    print("""
    1)          Balance
    2)          Withdraw
    3)          Deposit
    4)          Quit
    """)

    try:
        Option=int(input("Enter Option :"))

    except Exception as e:
        print("Error:",e)
        print("Enter 1,2,3 or 4 only")
        continue

    if Option==1:
        print("Balance $ ",balance)

    if Option==2:
        print("Balance $ ",balance)
        Withdraw=float(input("Enter Withdraw ammount $ :"))

        if Withdraw>0:
            forwardbalance=(balance-Withdraw)
            print("Forward balance is $ ",forwardbalance)

        elif Withdraw>balance:
            print("No Balance in account !!!")

        else:
            print("None withdraw made ")

    if Option==3:
        print("Balance $ ",balance)
        Deposit=float(input("Enter deposit ammount $ :"))

        if Deposit>0:
            forwardbalance=(balance+Deposit)
            print("forwardbalance $",forwardbalance)

        else:
            print("No deposit made !!!")
    
    if Option==4:
        exit()
