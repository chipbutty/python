#"Check primality - ex.11"
import random

num = range(1, 100)
b = random.choice(num)
print(b)


def is_prime(n):
    if n == 1:
        return True
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2
    while (i * i) <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True


flag = is_prime(b)
if (flag == True):
    print(b, "is a prime number")
else:
    print(b, "is NOT a prime number")