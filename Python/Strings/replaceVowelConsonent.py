def replace(s):
    s=list(s)
    n=len(s)
    v=['a','e','i','o','u','a']
    for i in range(n):
        if(s[i] in v):
            if(s[i]=="a"):
                s[i]="e"
            elif(s[i]=="e"):
                s[i]="i"
            elif(s[i]=="i"):
                s[i]="o"
            elif(s[i]=="o"):
                s[i]="u"
            elif(s[i]=="u"):
                s[i]="a"
        else:
            if(s[i]!="z"):
                s[i]=chr(ord(s[i])+1)
            else:
                s[i]="a"
    s="".join(s)
    return s
s=input("Enter string: ")
x=replace(s)
print(x)