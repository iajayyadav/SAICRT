

def fun(s):
    s1=""
    n=len(s)
    l=[]
    for i in range(n):
        if(s[i].isdigit()==True):
            s1=s1+s[i]
        if(s[i].isalpha()==True):
            if(s1!=""):
                l.append(s1)
                s1=""
        if(i==(n-1)):
            if(s1!=""):
                l.append(s1)
        m=len(l)
        l2=["0"]*m
        for i in range(m):
            l2[i]=int(l[i])
    return max(l2)
        
s=input("Enter string: ")
x=fun(s)
print(x)

    
            
    
