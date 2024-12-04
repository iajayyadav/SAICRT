def sumAscci(s):
    sum=0
    for i in s:
        sum=sum+(ord(i)-96)
    return sum

s=input("Enter string: ")
x=sumAscci(s)
print(x)