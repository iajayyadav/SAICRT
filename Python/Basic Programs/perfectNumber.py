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

n=int(input("Enter a number: "))
print(perfect(n))
