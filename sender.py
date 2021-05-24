import random
import time

from utils import UPPER_BOUND, LOWER_BOUND, bin_pow


class Sender:
    def __init__(self, g, p):
        self.g = g
        self.p = p
        self.__private_key = random.randint(UPPER_BOUND, LOWER_BOUND)
        self.__full_key = None

    def generate_partial_private_key(self):
        print(f"Let's check if bin_pow faster then built-in pow:")

        start = time.perf_counter_ns()
        res = bin_pow(self.g, self.__private_key, self.p)
        end = time.perf_counter_ns() - start
        print(f"Bin_pow: {end} ns")

        start = time.perf_counter_ns()
        res = pow(self.g, self.__private_key) % self.p
        end = time.perf_counter_ns() - start
        print(f"Built-in pow: {end} ns")

        return res

    def generate_full_private_key(self, partial_key):
        self.__full_key = bin_pow(partial_key, self.__private_key, self.p)

    def encrypt_message(self, msg):
        encrypted_msg = ""
        for c in msg:
            encrypted_msg += chr(ord(c) + self.__full_key)
        return encrypted_msg

    def decrypt_message(self, msg):
        decrypted_msg = ""
        for c in msg:
            decrypted_msg += chr(ord(c) - self.__full_key)
        return decrypted_msg
