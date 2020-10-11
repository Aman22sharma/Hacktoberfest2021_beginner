// AUTHOR: Syed Mohammad Muneer
// Python3 Concept: Creating Custom Exceptions(Explained using simple bank scenario)
// GITHUB: https: // github.com/muneersyed156


class Error(Exception):  # Inherit the Exception class to Error class
    pass


class LimitExceeded(Error):  # Inherit the Error class to create a custom Exception
    "Exception is rasied when user tries to with draw an amount greater than limit given by bank"
    pass


# Inherit the Error class to create a custom Exception
class InsufficientAmount(Error):
    "When a user tries to with draw more than his account's bank balance"
    pass


def Atm():  # Function denoting functionality of a simple ATM Machine
    limit = 5000  # limit of withdrawl is Rs.5000/-
    bankbalance = 10000  # Account balance is Rs.10000/-
    while(1):
        try:
            # Accepts input as integer
            a = int(input("Kindly enter the amount to be with drawn:"))
            if(a > limit):  # If requested amount is more than daily limit value then Exception is raised
                raise LimitExceeded
            if(a > bankbalance):  # If requested amount is more than account's balance then Exception is raised
                raise InsufficientAmount
        except LimitExceeded as e:  # LimitExceed exception is caught here
            print("Requested Amount is more than the limit,Kindly review your request!\n")
        except InsufficientAmount as e:  # Insufficient exception is caught here
            print(
                "Requested Amount exceeded your account balance,Kindly check your balance!\n")
        except Exception as e:  # Anyother Exceptions will be handeled here
            print(
                "Check the amount that you have entered.....Enter with out spaces.....and an integer value\n")
        else:  # else is executed when there is no exception raised in try block
            bankbalance -= a
            print("Remaining balance is {}".format(bankbalance))
            print("Your transaction is being processed.Please wait ..................\n")
        finally:  # finally will be executed irrespectives of any exceptions
            print("Thank you for visiting :)"+"....."+"To exit press ctrl+c\n")


if __name__ == "__main__":  # Main function
    Atm()  # ATM method is called here
