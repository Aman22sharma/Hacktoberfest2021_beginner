class Atm:
    pin=0
    __balance=0
    __counter=1001

    def __init__(self):
        self.accno=Atm.__counter
        self.pin=input("Kindly set ur pin:")
        print("Congrat pin set successfully!!")
        print("your account no is",self.accno)
        Atm.__counter=Atm.__counter+1
        
    @staticmethod
    def get_accno():
        return Atm.__accno
    def get_balance(self):
        print(self.__balance)

    def set_balance(self,value):
        if type(value)==int:
            self.__balance=value
            print("ho gaya")
        else:
            print("double",value)
    
    def changePin(self):
        temp=input("Purana pin kiya tha!!")
        if self.pin==temp:
            self.pin=input("Naya pin bata:")
            print("Ho gaya ")
        else:
            print("invalid pin")

    def deposit(self):
        temp=input("Enter ur pin:")
        if self.pin==temp:
            amount=int(input("Kitna deposit karna h"))
            self.__balance=self.__balance+amount
            print("Deposited")
        else:
            print("Jyada paise h kiya?")

    def checkBalance(self):
        temp=input("Enter ur pin:")
        if self.pin==temp:
            print("Your balance is",self.__balance)
        else:
            print("Dusree ka balance kyu jaana h!!")
              
    def withdraw(self):
        temp=input("Enter ur pin:")
        if self.pin==temp:
            amount=int(input("Kitna chahiye ??"))
            if amount<self.balance:
                self.__balance=self.__balance-amount
                print("Mil gaye naah?")
            else:
                print("Aukaad me rehna seekh lo,beta!!")
        else:
            print("chor!")

    


