import sys
from itertools import product
from random import shuffle
import time
import hashlib
from math import floor


sys.setrecursionlimit(1_000_000_000)

class bcolors:
    PASSWD = '\033[31m'
    STOCK = '\033[97m'


digits = [
    *[str(i) for i in range(0, 10)]
]

alpha = [
    *[chr(i) for i in range(ord('a'), ord('z') + 1)],
    *[chr(i) for i in range(ord('A'), ord('Z') + 1)]
]

charset_simple = [
    *[str(i) for i in range(0, 10)],
    *[chr(i) for i in range(ord('a'), ord('z') + 1)],
    *[chr(i) for i in range(ord('A'), ord('Z') + 1)]
]

charset_extended = [
    *[str(i) for i in range(0, 10)],
    *[chr(i) for i in range(ord('a'), ord('z') + 1)],
    *[chr(i) for i in range(ord('A'), ord('Z') + 1)],
    "-", "_", "+", "!", "@", "#", "$", "%", "^", "&", "*", "=", "!", "[", "]", "{", "}", "/", "?", ".", ",", "<", ">",
    ":", ";", "'", " ", "|"
]


def brute_force(charset, password, repeat):
    shuffle(charset)
    length = 1
    counter = 0
    t1 = time.perf_counter()
    for x in range(repeat ** length):
        idx = 1
        for generated in product(charset, repeat=length):
            gen = ''.join(generated)
            g = hashlib.sha256(gen.encode("utf-8")).hexdigest()
            print(f"{idx:,} | generated: {gen} |  {'SUCCESS' if g == password else 'FAIL'}")
            if g == password:
                break
            idx += 1
        else:
            counter += idx
            length += 1
            continue
        break
    t2 = time.perf_counter()
    print(f"{bcolors.PASSWD}password: {gen} {bcolors.STOCK} | hashed: {g}")
    print(f"c/s: {floor((counter - 1) / (t2 - t1))} | time: {round((t2 - t1), 5)}s | length: {length}")


if __name__ == "__main__":
    original = input("Password to find: ")
    passwd = hashlib.sha256(original.encode("utf-8")).hexdigest()
    print("Hashed password: ", passwd)
    '''passwd = input("Enter hash: ")'''
    mode = int(input("1 - digits\n2 - alpha\n3 - simple\n4 - extended\n"))
    if mode == 1:
        brute_force(digits, passwd, 10)
    elif mode == 2:
        brute_force(alpha, passwd, 52)
    elif mode == 3:
        brute_force(charset_simple, passwd, 62)
    elif mode == 4:
        brute_force(charset_extended, passwd, 92)