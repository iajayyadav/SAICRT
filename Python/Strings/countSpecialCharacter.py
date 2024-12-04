# Count number of special char in string
def countSpecial(s):
    count=0
    for i in s:
        if(i.isalnum()==True or i.isspace()==True):
            pass
        else:
            count+=1
    return count

s=input("Enter string: ")
x=countSpecial(s)
print(x)