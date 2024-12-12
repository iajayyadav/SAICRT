n= int(input("Enter no of elements: "))
arr=list(map(int,input("Enter elements: ").split()))
max1=arr[0]

for i in range(n):
    if(arr[i]>max1):
        max1=arr[i]
print(max1)

# 2nd Method

# x= max(arr)
# print(x)

