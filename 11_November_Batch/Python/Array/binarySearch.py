def binarySearch(n,arr,x):
    start=0
    end=n-1
    mid=(start+end)//2
    while(start<=end):
        if (arr[mid]==x):
            return True
        elif (x>arr[mid]):
            start=mid+1
            mid=(start+end)//2
        else:
            end=mid-1
            mid=(start+end)//2
    return False

n,x=map(int,input().split())
arr=list(map(int,input().split()))
ans=binarySearch(n,arr,x)
print(ans)