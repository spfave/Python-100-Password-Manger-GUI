# Password Generator Project
import random


# Constants
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# Functions
def generate_password():
    """ Generate random password, with random number of letters, numbers, and symbols """

    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    password_list = []
    [password_list.append(random.choice(letters)) for _ in range(nr_letters)]
    [password_list.append(random.choice(numbers)) for _ in range(nr_numbers)]
    [password_list.append(random.choice(symbols)) for _ in range(nr_symbols)]

    random.shuffle(password_list)
    password = "".join(password_list)
    # print(f"Your password is: {password}")

    return password
