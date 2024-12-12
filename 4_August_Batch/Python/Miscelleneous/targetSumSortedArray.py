def fun(arr, n, target):
    start=0
    end=n-1
    while(start<=end):
        sum=arr[start]+arr[end]
        if(target<sum):
            end-=1
        elif(target>sum):
            start+=1
        else:
            return True
    return False

n=int(input("Enter size: "))
arr=list(map(int,input("Enter elements: ").split()))
target=int(input("Enter target sum: "))
x=fun(arr,n,target)
print(x)
