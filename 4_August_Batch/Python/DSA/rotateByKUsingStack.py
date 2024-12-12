from collections import deque
stack=deque()
arr=[2,3,3,5,8,13,17,0,5,2]
for i in arr:
    stack.append(i)

n=int(input("Enter value to rotate: "))
stack.rotate(n)
arr=[]
for i in stack:
    arr.append(i)
print(arr)