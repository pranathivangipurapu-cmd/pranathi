# 10  --> 1 2 5 
# 50  --> 1 2 5 10 25
num=int(input("Enter your number to print factors :"))
for i in range(1, (num//2)+1):
    if num%i==0:
        print(i,end=" ")