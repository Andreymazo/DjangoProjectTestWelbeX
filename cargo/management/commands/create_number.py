import random
import string


# def unik_number_creation():
#     signs = []
#     for i in range(1, 4):
#         x = random.choice(string.ascii_letters.upper())
#         signs.append(x)
#     x = random.randint(0, 9)
#     signs.append(x)
#     xx = ''.join(str(x) for x in signs)
#     return xx
def unik_number_creation():
    signs = []
    for i in range(1, 4):
        x = random.randint(0, 9)
        signs.append(x)
    x = random.choice(string.ascii_letters.upper())
    signs.append(x)
    xx = ''.join(str(x) for x in signs)
    return xx
