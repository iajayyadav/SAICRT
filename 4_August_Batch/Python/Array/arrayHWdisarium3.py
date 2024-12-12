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

def disarium(n):
    sum=0
    count=0
    a=n
    while(n):
        count=count+1
        n=n//10
    n=a
    while(n):
        b=n%10
        sum=sum+(b**count)
        count=count-1
        n=n//10
    if(a==sum):
        return True
    return False


n=int(input("Enter number of elements: "))
arr=list(map(int,input("Enter the elements: ").split()))

sum=0

for i in range(n):
    x=prime(arr[i])
    if(x==True):
        sum=sum+arr[i]

y=disarium(sum)

if(y==True):
    print(True)
else:
    print(False)