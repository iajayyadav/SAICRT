from math import sqrt

def swapUsingThird(a,b):
    c=a
    a=b
    b=c
    print(a,b)

def swapWithoutUsingThird(a,b):
    a=a+b
    b=a-b
    a=a-b
    print(a,b)

def leapYear(n):
    if(n%400==0):
        return True
    elif(n%4==0 and n%100!=0):
        return True
    else:
        return False
    
def sumOfDigits(n):
    sum=0
    while(n!=0):
        b=n%10
        sum=sum+b
        n=n//10
    return sum

def reverseNumber(n):
    sum=0
    while(n!=0):
        b=n%10
        sum=(sum*10)+b
        n=n//10
    return sum

def palindrome(n):
    a=n
    sum=0
    while(n!=0):
        b=n%10
        sum=(sum*10)+b
        n=n//10
    if(sum==a):
        return True
    else:
        return False
    
def amstrongNumber(n):
    a=n
    count=0
    while(n!=0):
        count=count+1
        n=n//10
    n=a
    sum=0
    while(n!=0):
        b=n%10
        sum=sum+(b**count)
        n=n//10
    if(sum==a):
        return True
    else:
        return False
    
    
def factorial(n):
    fact=1
    while(n!=0):
        fact=fact*n
        n=n-1
    return fact

def spyNumber(n):
    sum=0
    prod=1
    while(n!=0):
        b=n%10
        sum=sum+b
        prod=prod*b
        n=n//10
    if(sum==prod):
        return True
    else:
        return False
    
def perfect(n):
    sum=0
    i=1
    while(i<=n//2):
        if(n%i==0):
            sum=sum+i
        i=i+1
    if(sum==n):
        return True
    return False

def prime(n):
    if(n<=1):
        return False
    i=2
    end=int(sqrt(n))
    for i in range(2,end+1,1):
        if(n%i==0):
            return False
    return True

def fibonacci(n):
    if(n==1):
        print(0)
    elif(n==2):
        print(0)
        print(1)
    else:
        print(0)
        print(1)
        n=n-2
        a=0
        b=1
        while(n!=0):
            c=a+b
            print(c)
            a=b
            b=c
            n=n-1





n=int(input("Enter number: "))
# m=int(input("Enter number: "))

print((n))