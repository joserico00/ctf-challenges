import random
import string

# List of random words
word_list = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape',
             'honeydew', 'icecream', 'jackfruit', 'kiwi', 'lime', 'mango', 'nectarine',
             'orange', 'pineapple', 'quince', 'raspberry', 'strawberry', 'tangerine',
             'ugli', 'victoria', 'watermelon', 'xigua', 'yellow', 'zucchini']

def generate_random_text(num_words=100000):
    words = [random.choice(word_list) for _ in range(num_words)]
    return ' '.join(words)

def hide_flag_in_text(text, flag, position):
    words = text.split()
    words.insert(position, flag)
    return ' '.join(words)

def main():
    random_text = generate_random_text()
    flag_position = random.randint(0, 100000)
    flag = "camp{your_flag_here}"
    text_with_flag = hide_flag_in_text(random_text, flag, flag_position)

    with open('challenge.txt', 'w') as f:
        f.write(text_with_flag)

    print("CTF setup complete. The challenge file is 'challenge.txt'")
    print("Find the hidden flag in the text file using grep!")

if __name__ == '__main__':
    main()

