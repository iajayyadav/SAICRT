def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
x=gcd(a,b)
print(x)