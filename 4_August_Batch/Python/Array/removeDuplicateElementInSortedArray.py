def fun(arr,n):
    if (n==1):
        return n
    index=1
    for i in range(1,n):
        if(arr[i]!=arr[i-1]):
            arr[index]=arr[i]
            index+=1
    return index

n= int(input("Enter no of elements: "))
arr=list(map(int,input("Enter elements: ").split()))
x=fun(arr,n)
for i in range(x):
    print(arr[i],end=" ")

