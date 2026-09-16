import os
import random
import shutil

def create_directories(base_dir, num_dirs):
    for i in range(num_dirs):
        os.makedirs(os.path.join(base_dir, f'dir{i}'), exist_ok=True)

def hide_flag(base_dir, num_dirs):
    hidden_dir = os.path.join(base_dir, f'dir{random.randint(0, num_dirs - 1)}')
    with open(os.path.join(hidden_dir, '.flag.txt'), 'w') as f:
        f.write('camp{your_flag_here}')

def main():
    base_dir = 'ctf_challengelevel2'
    num_dirs = 100

    # Clean up previous run
    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)

    create_directories(base_dir, num_dirs)
    hide_flag(base_dir, num_dirs)

    print(f"CTF setup complete. Base directory for challenges is './{base_dir}'")
    print(f"Find the hidden flag in one of the {num_dirs} directories!")

if __name__ == '__main__':
    main()

