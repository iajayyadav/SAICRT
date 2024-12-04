from math import sqrt

def factorial(n):
    fact=1
    while(n!=0):
        fact=fact*n
        n=n-1
    return fact

def digitsum(n):
    sum=0
    while(n):
        b=n%10
        sum=sum+b
        n=n//10
    return sum

def productOfDigits(n):
    prod=1
    while(n):
        b=n%10
        prod=prod*b
        n=n//10
    return prod

def palindrome(n):
    a=n
    sum=0
    while(n):
        b=n%10
        sum=(sum*10)+b
        n=n//10
    if(a==sum):
        return True
    return False

def spyNumber(n):
    if(digitsum(n)==productOfDigits(n)):
        return True
    return False

def swapTwo(a,b):
    c=a
    a=b
    b=c
    print(a,b)




def leapYear(n):
    if(n%400==0):
        return True
    elif(n%100==0):
        return False
    elif(n%4==0):
        return True

def sumOfNaturalNaumber(n):
    sum=0
    i=0
    while(i<=n):
        sum=sum+i
        i=i+1
    return sum

def sumOfSquares(n):
    sum=0
    i=1
    while(i<=n):
        sum=sum+(i*i)
        i=i+1
    return sum

def sumOfFactors(n):
    sum=0
    i=1
    while(i<=n//2):
        if(n%i==0):
            sum=sum+i
        i=i+1
    return sum

def totalDigit(n):
    count=0
    while(n):
        n=n//10
        count=count+1
    return count


def amstrongNumber(n):
    a=n
    count=0
    while(n):
        n=n//10
        count=count+1
    n=a
    sum=0
    while(n):
        b=n%10
        sum=sum+(b**count)
    if(sum==a):
        return True
    return False


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
    
def prime(n):
    if(n<=1):
        return False
    else:
        i=2
        end=int(sqrt(n))
        while(i<=sqrt(n)):
            if(n%i==0):
                return False
        return True
    



a = int(input("Enter: "))
fibonacci(a)
# n=int(input("Enter a number: "))
# print(factorial(n))
# print(digitsum(n))
# print(palindrome(n))
