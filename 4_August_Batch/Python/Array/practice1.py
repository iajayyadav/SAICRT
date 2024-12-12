def fun(arr,n):
    odd=0
    even=0
    for i in range(n):
        if(arr[i]%2==0):
            even=even+arr[i]
        else:
            odd=odd+arr[i]
    result=abs(odd-even)
    return result


n= int(input("Enter no of elements: "))
arr=list(map(int,input("Enter elements: ").split()))
x=fun(arr,n)
print(x)