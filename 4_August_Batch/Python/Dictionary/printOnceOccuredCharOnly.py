def frequency(s):
    d={}
    for i in s:
        d[i]=0
    for i in s:
        d[i]=d[i]+1
    for k in d.keys():
        if(d[k]==1):
            print(k,end="")
            
s=input("Enter string: ")
frequency(s)
