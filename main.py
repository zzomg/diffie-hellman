"""
Simple implementation for Diffie-Hellman cryptosystem
"""

from utils import generate_public_keys
from sender import Sender


def cryptosystem():
    p, g = generate_public_keys()

    Alice = Sender(p, g)
    Bob = Sender(p, g)

    print(f"Public keys are: {p}, {g}")

    message = "test message"

    # print(f"Secret message: {message}")

    alice_partial = Alice.generate_partial_private_key()
    bob_partial = Bob.generate_partial_private_key()

    print(f"Alice partial key: {alice_partial}")
    print(f"Bob partial key: {bob_partial}")

    Alice.generate_full_private_key(bob_partial)
    Bob.generate_full_private_key(alice_partial)

    assert Alice._Sender__full_key == Bob._Sender__full_key

    encrypted_msg = Alice.encrypt_message(message)
    print(f"Encrypted message: {encrypted_msg}")

    decrypted_msg = Bob.decrypt_message(encrypted_msg)
    print(f"Decrypted message: {decrypted_msg}")


if __name__ == '__main__':
    cryptosystem()
