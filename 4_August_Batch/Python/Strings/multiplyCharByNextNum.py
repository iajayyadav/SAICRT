def replace(s):
    n=len(s)
    s1=""
    for i in range(0,n-1,2):
        x=s[i]
        y=int(s[i+1])
        s1=s1+(x*y)
    return s1

s=input("Enter string: ")
x=replace(s)
print(x)
