def fib(n):
    if(n==0 or n==1):
        return n
    return fib(n-1) + fib(n-2)
n=int(input("Enter number of terms: "))
for i in range(n):
    x=fib(i)
    print(x)

# tower of hanoi
