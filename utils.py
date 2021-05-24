import sys
import random
import time
from math import sqrt
from functools import lru_cache

UPPER_BOUND = 500
LOWER_BOUND = 700  # let's consider bounds that are not too big for the sake of our experiment


def bin_pow(x, pow, modulo):
    number = 1
    while pow:
        if pow & 1:
            number = number * x % modulo
        pow >>= 1
        x = x * x % modulo
    return number


def is_prime(x):
    if x % 2 == 0:
        return False
    elif any(x % i == 0 for i in range(3, int(sqrt(x)) + 1, 2)):
        return False
    else:
        return True


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def primitive_root(p):  
    required_set = {num for num in range(1, p) if gcd(num, p)}
    prim_roots = [g for g in range(1, p) if required_set == {bin_pow(g, powers, p) for powers in range(1, p)}]
    g = random.choice(prim_roots)
    return g


def generate_random_prime():
    prime_list = [x for x in range(UPPER_BOUND, LOWER_BOUND) if is_prime(x)]
    p = random.choice(prime_list)
    return p


def generate_public_keys():
    print("Generating public keys...")

    start = time.time()
    p = generate_random_prime()
    end = time.time() - start
    print(f"Found first public key p {p} in {end}")

    start = time.time()
    g = primitive_root(p)
    end = time.time() - start
    print(f"Found second public key g {g} in {end}")

    return p, g
