arr = [10, 20, 30, 40, 50]
print(arr[2])
print(arr[-3])
# print(arr[5])
s = "Ajay"
print(s[2])
print(s)
s = "gaurav"
print(s)



# n= int(input("Enter number of elements: "))

# arr=list(map(int,input().split()))

# for i in range(0,n,1):
#     print(arr[i])
#     # print(arr[i],end=" ")



n=int(input("Enter number of elements: "))

arr=[]
for i in range(0,n):
    arr.append(int(input()))

for i in range(0,n):
    print(arr[i])

for i in arr:
    print(i)




