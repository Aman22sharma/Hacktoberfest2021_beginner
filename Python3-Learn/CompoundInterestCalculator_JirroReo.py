# AUTHOR: Jirro Reo
# Python3 Concept: A compound interest loan calculator
# Github: https://www.github.com/JirroReo

import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

class Account():
    lname = str()
    fname = str()
    mname = str()
    cstatus = str()
    pramount = float()
    rate = float()
    times = int()
    years = int()
    amount = float()

def askInput():
    c1 = Account()
    c1.lname = input('Enter the borrower\'s last name: ').upper()
    c1.fname = input('Enter the borrower\'s first name: ').upper()
    c1.mname = input('Enter the borrower\'s middle name: ').upper()
    c1.cstatus = input('Enter civil status: ').upper()
    c1.pramount = float(input('Enter principal amount: '))
    c1.rate = float(input('Enter the interest rate: '))
    c1.times = int(input('Enter the number of times the interest will be compounded: '))
    c1.years = int(input('Enter the number of years: '))
    c1.amount = c1.pramount * pow((1 + ((c1.rate/100)/c1.times)),c1.years)
    print('\n')
    return c1

def printReceipt(Account):
    print('Information\n')
    print('Name : {} {} {}'.format(Account.fname, Account.mname[:1], Account.lname))
    print('Civil Status : {}'.format(Account.cstatus))
    print('\n')
    print('Interest rate : \t{:.2f}%'.format(Account.rate))
    print('Times compounded : \t{}'.format(Account.times))
    print('Principal : \t\t{:.2f}'.format(Account.pramount))
    print('Interest : \t\t{:.2f}'.format(Account.amount - Account.pramount))
    print('Amount in savings : \t{:.2f}'.format(Account.amount))

if __name__ == "__main__":
    while True:
        clearConsole()
        print('----------------------------------------------------------------')
        printReceipt(askInput())
        print('----------------------------------------------------------------')
        ch = input('\nDo you want to input again? (y/n): ').upper()
        if ch == 'N':
            break