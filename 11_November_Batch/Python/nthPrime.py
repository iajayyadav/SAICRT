import math

def isPrime(n):
    if n <= 1:
        return False
    i = 2
    j = int(math.sqrt(n))
    while i <= j:
        if n % i == 0:
            return False
        i += 1
    return True


a = int(input("Enter the number: "))
count = 0
x = 2

while True:
    if isPrime(x):
        count += 1
    if count == a:
        print(x)
        break
    x += 1
