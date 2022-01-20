import random
import os

def read():
    with open("./data.txt", "r", encoding="utf-8") as f:
        global words
        words = [word.replace('\n','') for word in f]
    return words

def random_word():
    global rword
    rword= random.choice(words)
    rword= rword.rstrip()

def write():
    for letter in rword:
        print(letter.replace(letter, '_'), end=" ")
    
def comparation():
    letra=input('Ingresa una letra: ')
    for letter in rword:
        if letter == letra:
            print(letra)
        else:
            print('Try again!')

def run():
    pass


if __name__ == '__main__':
    print('Bienvenido al juego del ahorcado')
    print('Tienes que advinar la palabra' )    
    read()
    random_word()
    write()
    comparation()
    print(' ')


