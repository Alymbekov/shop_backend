import random
import string


def randomString(stringLangth=15):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLangth))
