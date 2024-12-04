# fun 1
# input: "I love you"
# output: "I evol uoy"

# fun 2
#input "He Loves You"
# output: "You Loves He"

def fun1(s):
    arr=s.split()
    n=len(arr)
    start=0
    end=n-1
    while(start<end):
        arr[start],arr[end]=arr[end],arr[start]
        start=start+1
        end=end-1
    s=" ".join(arr)
    return s

def fun2(s):
    arr=s.split()
    s1=""
    for i in arr:
        s1=s1+i[::-1]+" "
    return s1

def fun3(s):
    arr=s.split()
    for i in arr:
        print(i[::-1], end=" ")
        
s=input("Enter a string: ")
x=fun1(s)
y=fun2(s)
print(x)
print(y)
fun3(s)
