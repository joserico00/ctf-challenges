import hashlib
import os
import random
import string

def create_dictionary_file(dictionary_file, words, chosen_word):
    with open(dictionary_file, 'w') as f:
        for word in words:
            f.write(f'{word}\n')
        f.write(chosen_word)

def get_sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def main():
    dictionary_file = 'dictionary.txt'
    hashed_password_file = 'hashed_password.txt'
    
    words = [''.join(random.choices(string.ascii_letters, k=5)) for _ in range(1000)]
    chosen_word = 'yourword'  # replace with your own 8-letter password
    
    create_dictionary_file(dictionary_file, words, chosen_word)
    
    hashed_password = get_sha256_hash(chosen_word)
    
    with open(hashed_password_file, 'w') as f:
        f.write(hashed_password)

    print("CTF setup complete.")
    print(f"The dictionary file for the challenge is '{dictionary_file}' and the hashed password file is '{hashed_password_file}'")
    print("Find the password that matches the hashed password!")

if __name__ == '__main__':
    main()

