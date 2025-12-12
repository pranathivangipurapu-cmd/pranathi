
count=0
num=int(input("Enter your number to check it is prime or not :"))
for i in range(1, (num//2)+1):
    if num%i==0:
        count=count+1

if count==1:
    print(num," is a prime number")
else:
    print(num," is not a prime number")