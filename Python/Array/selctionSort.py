def selectionSort(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i]>arr[j]):

                arr[i],arr[j]=arr[j],arr[i]
    return arr


n=int(input("Enter no of element: "))
arr=list(map(int,input("Enter elements: ").split()))
x=selectionSort(arr,n)
print(x)