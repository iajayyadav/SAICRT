def linearSearch(arr,n,item):

    for i in range(n):
        if(arr[i]==item):
            return True
    return False
 
n=int(input("Enter number of elements: "))
arr=list(map(int,input("Enter ").split()))
item=int(input("Enter item to search: "))
x=linearSearch(arr,n,item)
print(x)