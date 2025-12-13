class ATM:
    acbal=10000
    def withdraw(self):
        amt=int(input("Enter your withdraw amount: "))
        if amt%100==0:
            if amt<=self.acbal:
                if amt<=20000:
                    self.acbal=self.acbal-amt
                else:
                    print("Transaction limit is 20k only")
            else:
                print("Insuffcient fund")
        else:
            print("Please enter multiples of 100")
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
        elif option==2:
            obj.withdraw()
        
            

obj=ATM()
obj.viewOptions()

        
        