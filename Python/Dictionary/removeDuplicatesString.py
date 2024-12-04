def removeDuplicates(s):
    d={}
    for i in s:
        d[i]=0
    s1=""
    for k in d.keys():
        s1=s1+k
    return s1
s=input("Enter a string: ")
x=removeDuplicates(s)
print(x)