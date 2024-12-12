def linearsearch(n,arr,x):
    for i in range(0,n,1):
        if arr[i]==x:
            return True
    return False

# 2nd Method

    # for i in arr:
    #     if i==x:
    #         return True
    # return False

# 3rd Method

    # if x in arr:

n,x=map(int,input().split())
arr=list(map(int,input().split()))
ans=linearsearch(n,arr,x)
if ans==True:
    print("YES")
else:
    print("NO")
