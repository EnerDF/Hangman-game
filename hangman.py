import random
import os

def read():
    words = [ ]
    with open("./data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line)
    print(words)

def run():
    pass


if __name__ == '__main__':
    read()