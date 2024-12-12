from math import sqrt


def avg(n, arr):
    sum = 0
    for i in range(n):
        sum = sum+arr[i]
    return sum/n


def amstrongNumber(n):
    a = n
    count = 0
    while (n):
        n = n//10
        count = count+1
    n = a
    sum = 0
    while (n):
        b = n % 10
        sum = sum+(b**count)
    if (sum == a):
        return True
    return False


def prime(n):
    if (n <= 1):
        return False
    else:
        i = 2
        end = int(sqrt(n))
        while (i <= sqrt(n)):
            if (n % i == 0):
                return False
            i=i+1
        return True


def arrFun(n, arr):
    average=avg(n,arr)
    if (average == int(average)):
        result= amstrongNumber(average)
        return result
    elif (average != int(average)):
        average=int(average)
        result= prime(average)
        return result


n = int(input("Enter no of elements: "))
arr = list(map(int, input("Enter elements: ").split()))
print(arrFun(n, arr))
