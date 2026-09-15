import hashlib
import os
import random
import string

def create_random_files(base_dir, num_files):
    for i in range(num_files):
        with open(os.path.join(base_dir, f'file{i+1}.txt'), 'w') as f:
            random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
            f.write(random_text)

def get_md5_hash(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
        return hashlib.md5(data).hexdigest()

def main():
    base_dir = 'cybercamphashes'
    num_files = 10

    # Clean up previous run
    if os.path.exists(base_dir):
        os.system(f'rm -rf {base_dir}')
    os.makedirs(base_dir, exist_ok=True)

    create_random_files(base_dir, num_files)

    chosen_file = os.path.join(base_dir, f'file{random.randint(1, num_files)}.txt')
    chosen_file_md5 = get_md5_hash(chosen_file)
    
    print(f"CTF setup complete. Base directory for challenges is './{base_dir}'")
    print(f"The MD5 hash of the chosen file is: {chosen_file_md5}")
    print(f"Find the file that matches the given MD5 hash!")

if __name__ == '__main__':
    main()

