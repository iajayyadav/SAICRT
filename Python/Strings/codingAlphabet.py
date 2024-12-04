def coding(s):
    s1=""
    for i in s:
        s1=s1+chr(122-ord(i)+97)
    return s1

    
s=input("Enter string: ")
x=coding(s)
print(x)

