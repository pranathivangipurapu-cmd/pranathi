num=6324
rev=0
while num!=0:            # 6!=0
    rem=num%10               # 6%10   =6
    rev=rev*10+rem       #4236
    num=num//10              # 6//10  6
print("reverse number: ",rev)