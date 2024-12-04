from math import sqrt
def prime(n):
    if(n<=1):
        return False
    i=2
    end=int(sqrt(n))
    for i in range(2,end+1,1):
        if(n%i==0):
            return False
    return True

n= int(input("Enter a number: "))
print(prime(n))