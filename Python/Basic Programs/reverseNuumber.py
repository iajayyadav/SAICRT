n=int(input("Enter a number: "))
a=n
sum=0
while(n):
    b=n%10
    sum=(sum*10)+b
    n=n//10
print(sum)

if(a==sum):
    print("Pelindrome")
else:
    print("Not a pelindrome")