from collections import deque
stack = deque()
s=input("Enter string: ")
for i in s:
    stack.append(i)
s1=""
while(len(stack)!=0):
    x=stack.pop()
    s1=s1+x
if(s==s1):
    print("Palindrome")
else:
    print("Not palindrome")