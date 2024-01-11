from functools import reduce

def prime_generator():
    yield 2
    num = 3
    while True:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 2


def factors(value):
    # primes = prime_generator()
    # factors = []
    # while value > 1:
    #     prime = next(primes)
    #     while value % prime == 0:
    #         factors.append(prime)
    #         value /= prime
    # return factors
    return fast_factors(value)

def find_factors(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:  # Avoid duplicates for perfect squares
                factors.append(n // i)
    factors.sort()  # Optional: Sort the factors for readability
    return factors

def filter_primes(numbers):
    primes = []
    for num in numbers:
        if num <= 1:
            continue  # 1 is not considered prime

        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

    return primes

def fast_factors(value):
    result = []
    while value > 1:
        f = find_factors(value)
        primes = filter_primes(f)
        while value % primes[0] == 0:
            result.append(primes[0])
            value /= primes[0]
    return result

examples = [120, 60, 30, 31,
            93819012551
            ]
# for example in examples:
#     print(example)
#     f = factors(example)
#     print(f)
#     print(reduce(lambda x, y: x * y, f))

for example in examples:
    print(example)
    print(fast_factors(example))
    print()
    # theres literally no way. I am capable of understand everything that is going on. but I can not for the life of me BE the person that is
    # the cause of the things that are going on. I'm only ever an observer. The harder you work the luckier you get. I'm not working at all right now
    # listen up dickheads, its a math video, everyone hecking loves math videos. Except you for some reason. Just hit the button what the fuck.

