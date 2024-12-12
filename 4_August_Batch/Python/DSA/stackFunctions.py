from collections import deque
stack = deque()
arr=[2,3,3,5,8,13,17,0,5,2]
for i in arr:
    stack.append(i)

# index function
x=stack.index(3,0,10)
print(x)

# insert function
stack.insert(4,6)
stack.insert(15,6)
print(stack)

#count function
x=stack.count(3)
print(x)

#remove function
stack.remove(5)
print(stack)

#extend function
arr1=[10,20,30,40]
# stack.extend(arr1)
stack.extendleft(arr1)
print(stack)

#revers function
stack.reverse()
print(stack)

# rotate function
stack.rotate()
