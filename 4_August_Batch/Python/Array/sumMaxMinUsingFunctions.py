
def sumOfArray(n,arr):
    sum=0
    for i in range(n):
        sum=sum+arr[i]
    return sum

def maxInArray(n,arr):
    max=arr[0]
    for i in range(n):
        if(arr[i]>max):
            max=arr[i]
    return max

def minInArray(n,arr):
    min=arr[0]
    for i in range(n):
        if(arr[i]<min):
            min=arr[i]
    return min


n= int(input("Enter no of elements: "))
arr=list(map(int,input("Enter elements: ").split()))
x=sumOfArray(n,arr)
print(x)
print(maxInArray(n,arr))
print(minInArray(n,arr))