def binarySearch(s,item):
    n=len(s)
    start=0
    end=n-1
    mid=(start+end)//2
    while(start<=end):
        if(s[mid]==item):
            return True
        elif(s[mid]<item):
            start=mid+1
            mid=(start+end)//2
        else:
            end=mid-1
            mid=(start+end)//2
    return False


s=input("Enter string: ")
item=input("Enter item to search: ")
x=binarySearch(s,item)
print(x)
