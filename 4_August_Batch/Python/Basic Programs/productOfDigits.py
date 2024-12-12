n=int(input("Enter a number: "))
prod=1
while(n!=0):
    b=n%10
    prod=prod*b
    n=n//10
print(prod)