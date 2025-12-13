def isPrime1(num):
    count=0
    a=False
    for i in range(1, (num//2)+1):
        if num%i==0:
            count=count+1
    if count==1:
       a=True
    
b=isPrime1(11)
if b==True:
    print("Prime number")
else:
    print("Not a prime number")

    
