def printSubString(s):
    n=len(s)
    for i in range(n):
        s1=""
        for j in range(i,n):
            s1=s1+s[j]
            print(s1)

s=input("Enter a string: ")
printSubString(s)