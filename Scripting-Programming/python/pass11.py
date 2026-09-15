from datetime import datetime

def get_flag():
    flag = "cybercamp{your_flag_here}"
    correct_date = datetime.now().date()
    user_date = datetime(2021, 1, 1).date()  # This line needs to be fixed

    if user_date == correct_date:
        print('Congratulations! Here is your flag:', flag)
    else:
        print('Wrong date. Try again.')

if __name__ == "__main__":
    get_flag()

