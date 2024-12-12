n=int(input("Enter a number: "))
a=n
count=0
while(n!=0):
    n=n//10
    count=count+1

sum=0
n=a
while(n):
    b=n%10
    sum=sum+(b**count)
    n=n//10

if(sum==a):
    print("Amstrong Number")
else:
    print("Not Amstrong")
    