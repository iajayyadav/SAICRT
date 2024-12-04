def inFibonacci(n):
    if(n==0 or n==1):
        return True
    a=0
    b=1
    while(1):
        c=a+b
        if(c==n):
            return True
        if(c>n):
            return False
        a=b
        b=c

n= int(input("Enter a number: "))
print(inFibonacci(n))