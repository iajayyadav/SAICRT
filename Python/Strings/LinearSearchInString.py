def linearSearch(s,ch):
    n=len(s)
    for i in range(n):
        if(s[i]==ch):
            return True
        
    return False

s=input("Enter string: ")
ch=input("Enter character to search: ")
x=linearSearch(s,ch)
print(x)