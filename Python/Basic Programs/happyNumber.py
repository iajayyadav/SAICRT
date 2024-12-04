def isHappy(n):
    sum=n
    while(sum>9):
        local=0
        while(sum!=0):
            b=sum%10
            local=local+(b*b)
            sum=sum//10
        sum=local
    if(sum==1 or sum==7):
        return True
    return False
n=int(input("Enter a number: "))
x=isHappy(n)
print(x)