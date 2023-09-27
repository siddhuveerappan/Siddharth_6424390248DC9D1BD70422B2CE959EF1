# A BankAccount Class Program

class BankAccount:
    # __accNum  : Account ID number
    # __accOwn  : Name of the account's owner
    # __accBal  : The amount stored in the account

    def __init__(self, aNumber, aOwner, aBalance):
        self.__accNum  = aNumber
        self.__accOwn  = aOwner

        if aBalance < 0:
            aBalance = 0

        self.__accBal  = aBalance

    def getBalance(self):
        return self.__accBal

    def displayBalance(self):
        print("Current Balance in account {} : {}".format(self.__accNum,self.__accBal))

    def deposit(self, amount):
        print("Attempting to deposit {} to account {}".format(amount, self.__accNum))
        if amount <= 0 :
            print("bad deposit amount value : {}".format(amount))
            return

        self.__accBal = self.__accBal + amount
        print("An amount of {} has been deposited".format(amount))

    def withdraw(self, amount):
        print("Attempting to withdraw {} from account {}".format(amount, self.__accNum))
        if amount <= 0 :
            print("bad withdraw amount value : {}".format(amount))
            return

        if amount > self.__accBal :
            print("Not enough balance")
            return

        self.__accBal = self.__accBal - amount
        print("An amount of {} has been withdrawn".format(amount))

def main():
    testAccount = BankAccount(1000, "Mr.Test", 2000)

    testAccount.displayBalance()
    testAccount.deposit(20)
    testAccount.displayBalance()
    testAccount.withdraw(666)
    testAccount.displayBalance()
    testAccount.withdraw(testAccount.getBalance())
    testAccount.displayBalance()
    testAccount.withdraw(20)
    testAccount.displayBalance()

if __name__ == "__main__" :
    main()
