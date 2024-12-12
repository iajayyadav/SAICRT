def is_automorphic(n):
    sq = n * n
    while n != 0:
        if n % 10 != sq % 10:
            return False
        n //= 10
        sq //= 10
    return True


a = int(input("Enter a number: "))
if is_automorphic(a):
    print("Automorphic")
else:
    print("Not Automorphic")

