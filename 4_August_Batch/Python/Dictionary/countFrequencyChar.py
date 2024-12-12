def frequency(s):
    d={}
    for i in s:
        d[i]=0
    for i in s:
        d[i]=d[i]+1
    for k,v in d.items():
        print(k," occured ",v,"times ")

s=input("Enter string: ")
frequency(s)
