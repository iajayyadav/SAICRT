def fun(arr,target):
    count=0
    d={}
    for i in arr:
        complement=target-i
        if(complement in d):
            count=count+d[complement]
        d[i]=d.get(i,0)+1
    return count

arr=list(map(int,input("Enter elements: ").split()))
target=int(input("Enter target: "))
x=fun(arr,target)
print(x)

# 5 times write both question
# learn 2sum
# https://www.geeksforgeeks.org/2sum/
