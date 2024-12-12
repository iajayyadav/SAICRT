# 1st method

def reverse1(s):
    return s[::-1]

# 2nd Method

def reverse2(s):
    s=list(s)
    start=0
    end=len(s)-1
    while(start<=end):
        s[start],s[end]=s[end],s[start]
        start=start+1
        end=end-1
    s="".join(s)
    return s

# 3rd Method

def reverse3(s):
    n=len(s)-1
    i=0
    s1=""
    # while(i<=n):
    #     s1=s1+s[n]
    #     n=n-1
    # using for loop
    for i in range(n,-1,-1):
        s1=s1+s[i]
    return s1



s=(input("Enter string: "))
x=reverse3(s)
print(x)

        
