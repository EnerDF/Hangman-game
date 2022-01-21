import random
import os

def read():
    with open("./data.txt", "r", encoding="utf-8") as f:
        global words
        words = [word.replace('\n','') for word in f]
    return words

def random_word():
    global rword
    rword = random.choice(words)
    rword = rword.rstrip()  
    sentence = rword
    translate_rword = rword.maketrans('áéíóú', 'aeiou')
    rword = rword.translate(translate_rword)
    print(rword)

def write():
    for letter in rword:
        print(letter.replace(letter, '_'), end=" ")
    
def wlist():
    global lrword, drword, dgword
    lrword = list(rword)
    drword= {i: lrword[i] for i in range(0, len(lrword))}
    dgword= {i: lrword[i].replace(lrword[i], '_') for i in range(0, len(lrword))}

def comparation():
    global user_letter
    print(' ')
    user_letter= input('Ingresa una letra: ')
    lives = 5
    for i in drword:
        if user_letter == drword[i]:
            dgword.update({i: user_letter})
    for key, value in dgword.items():
        print(value, end=" ")
            
# def comparation():
#     print(' ')
#     letra=input('Ingresa una letra: ')
#     i = rword.find(letra)
#     for letter in rword:
#         if letter == letra:
#             print(letra)
#         else:drword[letter]
#             print('Try again!')

def run():
    pass


if __name__ == '__main__':
    print('Bienvenido al juego del ahorcado')
    print('Tienes que advinar la palabra' )    
    read()
    random_word()
    write()
    wlist()
    comparation()


