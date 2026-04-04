class BankAccount:
    ROI = 10.5

    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("name of account holder : ",self.Name)
        print("Current Account balance is : ",self.Amount)

    def Deposit(self):
        deposit = int(input("Enter the amount that you want to deposit : "))
        self.Amount = self.Amount + deposit

    def Withdraw(self):
        withdraw = int(input("Enter the amount that you want to withdraw : "))

        if(self.Amount < withdraw):
            print("Insufficient Balance")
        else:

            self.Amount = self.Amount - withdraw

    def CalculateIntrest(self):
        Intrest = self.Amount * BankAccount.ROI / 100
        return Intrest
    
bobj1 = BankAccount("Sakshi",300)
bobj1.Display()
bobj1.Deposit()
bobj1.Withdraw()
bobj1.Display()
Iret = bobj1.CalculateIntrest()
print("Intrest is : ",Iret)

