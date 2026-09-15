import random

def get_flag():
    flag = "cybercamp{your_flag_here}"
    correct_number = random.randint(1, 10)
    guessed_number = 0  # This line needs to be fixed Hint:you dont need to actualy guess the number

    if guessed_number == correct_number:
        print('Congratulations! Here is your flag:', flag)
    else:
        print('Incorrect number. Try again.')

if __name__ == "__main__":
    get_flag()

