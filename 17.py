class ATM:
    def viewOptions(self):
        pritn("Welcome to ABC bank ")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance Enquiry")
        print("0. EXIT")
class ATM:
    acbal=10000
    def deposit(self):
        amt=int(input("Enter your deposite amount :"))
        self.acbal=self.acbal+amt
        print("Avaliable bal is: ",self.acbal) 
        
        
    def viewOptions(self):
        print("Welcome to ABC bank ")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance Enquiry")
        print("0. EXIT")
        option=int(input("Choose your option: "))
        if option==1:
            obj.deposit()
            

obj=ATM()
obj.viewOptions()
        option=int(input("Choose your option: "))