def secondHighest(n,arr):
    highest=float("-inf")
    second=float("-inf")
    for i in range(n):
        if(arr[i]>highest):
            second=highest
            highest=arr[i]
        elif(arr[i]>second and arr[i]!=highest):
            second=arr[i]
    if(second==float("-inf")):
        return -1
    return second

n=int(input("Enter number of elements: "))
arr=list(map(int,input("Enter elements: ").split()))
x= secondHighest(n,arr)
print("Second highest is ",x)
