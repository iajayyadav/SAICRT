#printing first n terms of fibonacci series

def fibonacci(n):
    if(n==1):
        print(0)
    elif(n==2):
        print(0)
        print(1)
    else:
        print(0)
        print(1)
        n=n-2
        a=0
        b=1
        while(n):
            c=a+b
            print(c)
            a=b
            b=c
            n=n-1
    
n=int(input("Enter the number of terms: "))
fibonacci(n)
