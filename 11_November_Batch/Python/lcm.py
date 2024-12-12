def lcm(a, b):
    if a == b:
        return a
    if a < b:
        max_value = b
    if b < a:
        max_value = a

    i = max_value
    while True:
        if max_value % a == 0 and max_value % b == 0:
            return max_value
        max_value += i


a = int(input("Enter first number: "))
b = int(input("Enter first number: "))
ans = lcm(a,b)
print(ans)
