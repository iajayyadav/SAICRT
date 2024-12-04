from math import sqrt
def isSunny(n):
    n+=1
    x=sqrt(n)
    y=int(x)
    if(x==y):
        return True
    return False

n=int(input("Enter number: "))
x=isSunny(n)
print(x)