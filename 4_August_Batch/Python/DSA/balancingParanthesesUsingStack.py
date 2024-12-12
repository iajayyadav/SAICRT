from collections import deque


def check(str):
    stack = deque()
    for i in str:
        if ((i in "]})") and (len(stack) == 0)):
            return False
        elif ((i in "{[(")):
            stack.append(i)
        elif (((stack[-1] == "[") and (i == "]")) or ((stack[-1] == "{") and (i == "}")) or ((stack[-1] == "(") and (i == ")"))):
            stack.pop()
        else:
            stack.append(i)
    if (len(stack) == 0):
        return True
    return False


str = input("Enter string: ")
x = check(str)
print(x)
