def arraysum(n,arr):
    sum=0
    for i in range(n):
        sum=sum+arr[i]
    return sum

n=int(input())
arr=list(map(int,input().split()))
ans=arraysum(n,arr)
print(ans)