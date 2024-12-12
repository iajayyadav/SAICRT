def bubbleSort(arr,n):
    count=0
    for i in range(n):
        swapped=0
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped =1
        count=count+1
        if(swapped==0):
            break
    print(count)
    return arr

n=int(input("Enter number of elements: "))
arr=list(map(int,input("Enter ").split()))
x=bubbleSort(arr,n)
print(x)
