def factorial(a):
    fact=1
    while(a):
        fact=fact*a
        a=a-1
    return fact

def isStrong(a):
    sum=0
    n=a
    while(a):
        b=a%10
        sum=sum+factorial(b)
        a=a//10
    if (sum==n):
        return True
    return False

n= int(input("Enter a number: "))
ans= isStrong(n)
print(ans)