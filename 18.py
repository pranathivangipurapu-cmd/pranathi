class ATM:
    acbal=10000
    def deposit(self):
        amt=int(input("Enter your deposite amount :"))
        if amt%100==0:
            if amt<=50000:
                self.acbal=self.acbal+amt
            else:
                print("Transaction limit is 50k only")
        else:
            print("Please enter multiples of 100")
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

        
        