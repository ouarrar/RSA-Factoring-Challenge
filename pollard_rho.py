import math
import random

def pollard_rho(n):
    if n % 2 == 0:
        return 2

    x = random.randint(1, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1

    def f(x):
        return (x * x + c) % n

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = math.gcd(abs(x - y), n)

    return d

n = 239821585064027
p = pollard_rho(n)
q = n // p

print("p =", p)
print("q =", q)

