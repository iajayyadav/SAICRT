def pairSum(n,arr,k):
    count=0
    for i in range(n):
        for j in range(i+1,n):
            if((arr[i]+arr[j])==k):
                count=count+1
    return count



n=int(input("Enter number of elements: "))
arr=list(map(int,input("Enter elements: ").split()))
k=int(input("Sum= "))
x=pairSum(n,arr,k)
print(x,"pairs")