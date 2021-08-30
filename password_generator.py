#By @nachosaborio

import random
import string


def generate():
    characters = string.ascii_letters + string.punctuation + string.digits
    password_list = []
    
    for i in range(15):
        random_char = random.choice(characters)
        password_list.append(random_char)
        
    password_list = ''.join(password_list)
    return password_list


def run():
    password = generate()
    print("Your password is: " + password)


if __name__ == "__main__":
    run()