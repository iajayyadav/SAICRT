def stringFun(s):
    n=len(s)
    if(n%2==0):

        s1=s[:(n//2)-1]
        s2=s[(n//2)+1:]
        print(s1+s2)
    else:
        s1=s[:(n//2)]
        s2=s[(n//2)+1:]
        print(s1+s2)

s=input("Enter string: ")
stringFun(s)