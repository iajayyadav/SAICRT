def specialChar(s):
    count=0
    for i in s:
        if(i.isalnum()==False and i.isspace()==False):
            count+=1
    return count
s=input("Enter string: ")
x=specialChar(s)
print(x)