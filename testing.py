import time

from utils import generate_random_prime_naive, generate_random_prime_erat, primitive_root
from utils import bin_pow
from utils import LOWER_BOUND, UPPER_BOUND


# Let's simulate the work of the program with some pre-defined data to evaluate its efficiency.
#
#
#
# Let's compare two algorithms for generating a random prime number:
#   1. First one is a naive algorithm which checks all numbers inside an interval for primitivity,
#       with slight enhancements (skipping even numbers + stopping iterations on square root of a number)
#   2. Second one is an implementation of Sieve of Eratosthenes algorithm.
# Second algorithm is supposed to be more efficient.


s1 = time.perf_counter_ns()
p = generate_random_prime_naive(LOWER_BOUND, UPPER_BOUND)
e1 = time.perf_counter_ns() - s1
print(f"Naive impl: {e1} ns")

s2 = time.perf_counter_ns()
p = generate_random_prime_erat(LOWER_BOUND, UPPER_BOUND)
e2 = time.perf_counter_ns() - s2
print(f"Erat impl: {e2} ns")


# Algorithm of finding primitive roots of a number has most complexity so far,
# which leads the whole cryptosystem to have this complexity O(p^2)
g = primitive_root(p)

# Now let's compare several ways to take powers.
#   1. Built-in pow() function.
#   2. Built-in ** operator.
#   3. Binary exponentiation.
# Last one is supposed to be more efficient.

private_key = 1337420

s1 = time.perf_counter_ns()
res = bin_pow(g, private_key, p)
e1 = time.perf_counter_ns() - s1
print(f"Bin_pow: {e1} ns")

s2 = time.perf_counter_ns()
res = pow(g, private_key) % p
e2 = time.perf_counter_ns() - s2
print(f"Built-in pow: {e2} ns")

s3 = time.perf_counter_ns()
res = g ** private_key % p
e3 = time.perf_counter_ns() - s3
print(f"Built-in **: {e3} ns")


