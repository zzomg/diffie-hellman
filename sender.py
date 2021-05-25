import random

from utils import UPPER_BOUND, LOWER_BOUND, bin_pow


class Sender:
    def __init__(self, g, p):
        self.g = g
        self.p = p
        self.__private_key = random.randint(LOWER_BOUND, UPPER_BOUND)
        self.__full_key = None

    def generate_partial_private_key(self):
        return bin_pow(self.g, self.__private_key, self.p)

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
