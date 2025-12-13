def viewPrograms():
    print("1. Prime number program")
    print("2. Reverse of a given number")
    print("3. Print factors of a given number")
    option=int(input("Choose your option: "))
    if option==1:
        isPrime()
    elif option==2:
        reverseNumber()
    elif option==3:
        factors()
    else:
        print("Please select 1 to 3")
def isPrime():
    print("Prime number program")
def reverseNumber():
    print("Reverse number code")
def factors():
    print("Factors code")


viewPrograms()
    