n=int(input("Enter a number: "))
sum=0
prod=1
while(n!=0):
    b=n%10
    sum=sum+b
    prod=prod*b
    n=n//10

if(sum==prod):
    print("Spy Number")
else:
    print("Not Spy Number")

