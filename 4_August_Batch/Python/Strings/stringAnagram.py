def isAnagram(s1,s2):
    if(sorted(s1)==sorted(s2)):
        return True
    return False


s1=input("Enter 1st string: ")
s2=input("Enter 2nd string: ")
x=isAnagram(s1,s2)
print(x)