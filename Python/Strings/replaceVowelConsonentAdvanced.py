def replace(s):
    def replaceVowel(s):
        v = ["a", "e", "i", "o", "u", "a"]
        s = list(s)
        s1 = ""
        for i in s:
            for j in range(5):
                if (i == v[j]):
                    s1 = s1+v[j+1]
        return s1

    v = ["a", "e", "i", "o", "u", "a"]
    s2 = ""
    for i in s:
        if (i in v):
            x = replaceVowel(i)
            s2 = s2+x
        else:
            y=chr(ord(i)+1)
            if(y in v):
                x=replaceVowel(y)
                s2=s2+x
            else:
                s2=s2+y
    return s2
   


s = input("Enter string: ")
x = replace(s)
print(x)
