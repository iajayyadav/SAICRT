n= int(input("Enter no of elements: "))
arr=list(map(int,input("Enter elements: ").split()))
min1=arr[0]

#  1st Method

# for i in range(n):
#     if(arr[i]<min1):
#         min1=arr[i]
# print(min1)

# 2nd Method

x= min(arr)
print(x)