def fun(arr,n):
    presum={}
    sum=0
    max_len=0
    for i in range(n):
        sum+=arr[i]
        if(sum==0):
            max_len=i+1
        if(sum in presum):
            max_len=max(max_len,(i-presum[sum]))
        else:
            presum[sum]=i
    return max_len

n=int(input("Enter size: "))
arr=list(map(int,input("Enter elements: ").split()))
x=fun(arr,n)
print(x)

        
