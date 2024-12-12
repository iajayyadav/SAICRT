n=int(input("No. of elements: "))
arr=list(map(int,input("Enter elements: ").split()))
sum1=0
# 1st Method :

for i in range(n):
    sum1=sum1+arr[i]
print(sum1)


# 2nd Method :

# for i in arr:
#     sum1=sum1+i
# print(sum1)

# 3rd Method :

# x=sum(arr)
# print(x)