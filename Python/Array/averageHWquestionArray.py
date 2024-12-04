# find average of array , 
# if average is int then check if average is amstrong 
# elif average is float then convert it into int and
# check if average is prime

def arrayFun(n,arr):
    sum=0
    for i in range(n):
        sum=sum+arr[i]
    avg=sum/n

    if(avg==int(avg)):
        count=0
        a=avg
        while(avg):
            count=count+1
            avg=avg//10
        avg=a
        amstrong=0
        while(avg):
            b=avg%10
            amstrong=amstrong+(b**count)
            avg=avg//10
        if(amstrong==a):
            return True
        return False
    elif(avg!=int(avg)):
        avg=int(avg)
        if(avg<=1):
            return False
        else:
            i=2
            while(i**2<=avg):
                if(avg%i==0):
                    return False
                i=i+1
            return True


            



n= int(input("Enter no of elements: "))
arr=list(map(int,input("Enter elements: ").split()))

print(arrayFun(n,arr))

