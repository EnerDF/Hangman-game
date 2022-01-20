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
    print(rword)

def write():
    for letter in rword:
        print(letter.replace(letter, '_'), end=" ")
    
def wlist():
    lrword = list(rword)
    lrword = list(enumerate(lrword))

def comparation():
    print(' ')
    letra=input('Ingresa una letra: ')
    i = rword.find(letra)
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
    wlist()
    print(' ')


