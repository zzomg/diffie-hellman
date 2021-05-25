import random
import time
from math import sqrt

LOWER_BOUND = 500*2
UPPER_BOUND = 700*2  # let's consider not too big for the sake of our experiment


def bin_pow(x, pow, modulo):  # only supports integer exponentiation; O(log pow)
    n = 1
    while pow:
        if pow & 1:
            n = n * x % modulo
        pow >>= 1
        x = x * x % modulo
    return n


def is_prime(x):  # O(sqrt(x))
    if x % 2 == 0 and x != 2:
        return False
    elif any(x % i == 0 for i in range(3, int(sqrt(x)) + 1, 2)):
        return False
    else:
        return True


def gcd(a, b):  # Euclidean algorithm; O(log(min(a, b))
    while b != 0:
        a, b = b, a % b
    return a


def primitive_root(p):  # O(p^2)
    required_set = {num for num in range(1, p) if gcd(num, p)}
    prim_roots = [g for g in range(1, p) if required_set == {bin_pow(g, powers, p) for powers in range(1, p)}]
    return random.choice(prim_roots)


def generate_random_prime_erat(lower_bound,
                               upper_bound):  # Sieve of Eratosthenes starting with half-sieve; O(n log log n)
    sieve = [True] * (upper_bound // 2)
    for i in range(3, int(upper_bound ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2:: i] = [False] * ((upper_bound - i * i - 1) // (2 * i) + 1)
    res = [2] + [2 * i + 1 for i in range(1, upper_bound // 2) if sieve[i]]
    return random.choice([x for x in res if x >= lower_bound])  # O (upper bound)


def generate_random_prime_naive(lower_bound, upper_bound):
    prime_list = [x for x in range(lower_bound, upper_bound) if is_prime(x)]  # O (upper bound)
    return random.choice(prime_list)  # O(1)


def generate_public_keys():
    print("Generating public keys...")

    start = time.perf_counter()
    p = generate_random_prime_erat(LOWER_BOUND, UPPER_BOUND)
    end = time.perf_counter() - start
    print(f"Found first public key p {p} in {end}")

    start = time.perf_counter()
    g = primitive_root(p)
    end = time.perf_counter() - start
    print(f"Found second public key g {g} in {end}")

    return p, g
