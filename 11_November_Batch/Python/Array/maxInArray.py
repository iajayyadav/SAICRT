def maximum(n,arr):
    max=arr[0]
    for i in range(1,n):
        if arr[i]>max:
            max=arr[i]
    return max

n=int(input())
arr=list(map(int,input().split()))
ans=maximum(n,arr)
print(ans)