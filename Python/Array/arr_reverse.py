n= int(input("Enter number: "))
arr=[]
for i in range(0,n):
    arr.append(int(input()))

print("Reverse array: ")

for i in range(n-1,-1,-1):
    print(arr[i])