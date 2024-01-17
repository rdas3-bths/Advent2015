
import math

def get_factors(x):
    factors = []
    for i in range(1, x + 1):
       if x % i == 0:
           factors.append(i)
    return factors

def get_number_of_divisors(x):
    small_divisors = [i for i in range(1, int(math.sqrt(x)) + 1) if x % i == 0]
    large_divisors = [x / d for d in small_divisors if x != d * d]
    return small_divisors + large_divisors

presents = 0
i = 0
print("Part 1:")
while True:
    divisors = get_number_of_divisors(i)
    presents = sum(divisors) * 10
    if presents >= 29000000:
        print("House", i, ":", end="")
        print(presents, "presents")
        break
    i += 1

print("Part 2:")
i = 0
while True:
    divisors = get_number_of_divisors(i)
    divisors = [d for d in divisors if i / d <= 50]
    presents = sum(divisors) * 11
    if presents >= 29000000:
        print("House", i, ":", end="")
        print(presents, "presents")
        break
    i += 1


