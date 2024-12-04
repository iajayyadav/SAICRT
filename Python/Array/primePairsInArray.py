from math import sqrt
def isPrime(n):
    if(n<=1):
        return False
    i=2
    end=int(sqrt(n))
    while(i<=end):
        if(n%i==0):
            return False
        i=i+1
    return True
def pairPrime(n,arr):
    count=0
    for i in range(n):
        for j in range(i+1,n):
            x=isPrime(arr[i])
            y=isPrime(arr[j])
            if(x==True and y==True):
                count=count+1
    return count

n=int(input("Enter number of elements: "))
arr=list(map(int,input("Enter elements: ").split()))
x=pairPrime(n,arr)
print(x)


