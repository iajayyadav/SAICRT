def fun(s):
    alpha=""
    digit=""
    for i in s:
        if(i.isalpha()==True):
            alpha=alpha+i
        elif(i.isdigit()==True):
            digit=digit+i
    return alpha+digit

# arrange in sorted form
def fun2(s):
    alpha=""
    digit=""
    for i in s:
        if(i.isalpha()==True):
            alpha=alpha+i
        elif(i.isdigit()==True):
            digit=digit+i
    alpha=sorted(alpha)
    digit=sorted(digit)
    s1=alpha+digit
    s1="".join(s1)
    return s1



s=input("Enter string: ")
x=fun(s)
y=fun2(s)
print(x)  
print(y) 