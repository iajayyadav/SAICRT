def binarySearch(n,arr,item):
    start=0
    end=n-1
    mid=(start+end)//2
    while(start<=end):
        if(arr[mid]==item):
            return True
        elif(item<arr[mid]):
            end=mid-1
            mid=(start+end)//2
        else:
            start=mid+1
            mid=(start+end)//2
    return False

n=int(input("Enter number of elements: "))
arr=list(map(int,input("Enter ").split()))
item=int(input("Enter item to search: "))
x=binarySearch(n,arr,item)
print(x)


