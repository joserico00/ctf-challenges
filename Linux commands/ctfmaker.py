
import os
import shutil

def setup_ctf_folder():
    base_dir = 'ctf_challenge'
    flag_dir = os.path.join(base_dir, 'flags')

    # Clean up previous run
    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)

    # Create directories
    os.makedirs(flag_dir)

    # Create files and flags
    with open(os.path.join(flag_dir, 'flag1.txt'), 'w') as f:
        f.write('CYBERCAMP{your_flag_here}')

    # the searchable marker task 2 asks for, in a hidden file so players need grep -r
    with open(os.path.join(flag_dir, '.flag2.txt'), 'w') as f:
        f.write('THIS_IS_A_SECRET_MESSAGE\nCYBERCAMP{your_flag_here}')

    # Return path of directory to be used in the third task
    return flag_dir


def main():
    flag_dir = setup_ctf_folder()
    print(f"CTF setup complete. Base directory for challenges is './ctf_challenge'")

    print("Flag 1: Find a file named 'flag1.txt'.")
    print("Flag 2: Find a file which contains 'THIS_IS_A_SECRET_MESSAGE'.")
    print(f"Flag 3: Determine the number of files in the directory: '{flag_dir}'. The flag is 'FLAG{{number_of_files}}'. Replace 'number_of_files' with the actual number.")


if __name__ == '__main__':
    main()

