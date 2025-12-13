class ATM:
    acbal=10000
    def continue1(self):
        value=int(input("1 for continue and 0 for EXIT"))
        if value==1:
            obj.viewOptions()
        else:
            print("Thank you, Visit again")
    def numberOfNotes(self,amt):
        five=0
        two=0
        one=1
        if amt>=500:
            five=amt//500
            amt=amt-(five*500)
            print("500 rupees notes are : ",five)
        if amt>=200:
            two=amt//200
            amt=amt-(two*200)
            print("200 rupees notes are : ",two)
        if amt>=100:
            print("100 rupees notes are  ",one)
            
    def withdraw(self):
        amt=int(input("Enter your withdraw amount: "))
        if amt%100==0:
            if amt<=self.acbal:
                if amt<=20000:
                    self.acbal=self.acbal-amt
                    obj.numberOfNotes(amt)
                    print("Avaliable bal is: ",self.acbal) 
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
            obj.continue1()
        elif option==2:
            obj.withdraw()
            obj.continue1()
        elif option==3:
            print("Avaliable bal is: ",self.acbal)
            obj.continue1()
        elif option==0:
            print("Thank you, Visit again")
        else:
            print("Please select correct option ")
        
            

obj=ATM()
obj.viewOptions()

        
        