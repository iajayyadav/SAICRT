from math import sqrt


def prime(n):
    if (n <= 1):
        return False
    i = 2
    end = int(sqrt(n))
    while (i <= end):
        if (n % i == 0):
            return False
        i = i+1
    return True


def digitSum(n):
    sum = 0
    while (n):
        b = b % 10
        sum = sum+b
        n = n//10
    return sum


def reverse(n):
    sum = 0
    while (n):
        b = n % 10
        sum = (sum*10)+b
        n = n//10
    return sum


def isEven(n):
    if (n % 2 == 0):
        return True
    return False


def amstrong(n):
    count = 0
    a = n
    while (n):
        count = count+1
        n = n//10
    n = a
    sum = 0
    while (n):
        b = n % 10
        sum = sum+(b**count)
        n = n//10
    if (a == sum):
        return True
    return False


n = int(input("Enter no of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

evenSum = 0
oddSum = 0
for i in range(n):
    x = isEven(arr[i])
    if (x == True):
        evenSum = evenSum+arr[i]
    else:
        oddSum = oddSum+arr[i]

difference = abs(evenSum-oddSum)

y = isEven(difference)

if (y == True):
    a = reverse(difference)
    b = a+5
    print(prime(b))

else:
    c = prime(difference)
    if (c == True):
        print(True)
    else:
        d = amstrong(difference)
        if (d == True):
            print(True)
        else:
            print(False)
