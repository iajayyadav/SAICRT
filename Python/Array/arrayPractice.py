from math import sqrt
def prime(n):
    if(n<=1):
        return False
    i=2
    end=int(sqrt(n))
    while(i<=end):
        if(n%i==0):
            return False
        i=i+1
    return True
def isEven(n):
    if(n%2==0):
        return True
    return False
def reverse(n):
    sum=0
    while(n):
        b=n%10
        sum=(sum*10)+b
        n=n//10
    return sum
def digitSum(n):
    sum=0
    while(n):
        b=n%10
        sum=sum+b
        n=n//10
    return sum
def palindrome(n):
    a=reverse(n)
    if(a==n):
        return True
    return False

n= int(input("Enter no of elements: "))
arr=list(map(int,input("Enter elements: ").split()))

sum=0

for i in range(n):
    x=prime(arr[i])
    if(x==True):
        sum=sum+arr[i]
       

y=isEven(sum)

if(y==True):
    z=reverse(sum)
    print(z)
else:
    m=palindrome(sum)
    if(m==True):
        print(sum)
    else:
        n=digitSum(sum)
        print(n)

    
    