from datetime import datetime
import random
from random import randrange


def generate_birthday() -> datetime:
    """
    Make random date to use as birthday
    """

    year = randrange(1900, 1990)
    month = randrange(1, 12)
    day = randrange(1, 30)

    birthday = datetime(year, month, day)

    return birthday


def generate_password(length=20) -> str:
    """
    Generate a password
    """

    chars ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+}{"

    password=""

    for i in range(length+1):
        password += random.choice(chars)

    return password