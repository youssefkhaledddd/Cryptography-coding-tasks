import itertools
import string

def decrypt(ciphertext, key):
    alphabet = string.ascii_lowercase
    key_map = {k: v for k, v in zip(key, alphabet)}
    return ''.join(key_map.get(char, char) for char in ciphertext.lower())

def brute_force_monoalphabetic(ciphertext):
    alphabet = string.ascii_lowercase
    for perm in itertools.permutations(alphabet):
        decrypted_text = decrypt(ciphertext, perm)
        print(f"Possible Decryption: {decrypted_text}")

if __name__ == "__main__":
    encrypted_message = input("Enter the encrypted message: ")
    brute_force_monoalphabetic(encrypted_message)
 