from random import choice
from string import ascii_uppercase, ascii_lowercase, digits


def random_string(length=8):
    # Returns a string of default length 8
    return ''.join(choice(ascii_uppercase + ascii_lowercase + digits)
                   for _ in range(length))


def random_num_string(length=8):
    # Returns a string of default length 8 consisting of only digits
    return ''.join(choice(digits) for _ in range(length))
