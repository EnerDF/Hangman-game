import random
from os import system


def read():
    with open("./data.txt", "r", encoding="utf-8") as f:
        global words
        words = [word.replace('\n','') for word in f]
    return words

def random_word():
    global rword
    rword = random.choice(words)
    rword = rword.rstrip()  
    translate_rword = rword.maketrans('áéíóú', 'aeiou')
    rword = rword.translate(translate_rword)
    
def wlist():
    global lrword, drword, dgword
    lrword = list(rword)
    drword= {i: lrword[i] for i in range(0, len(lrword))}
    dgword= {i: lrword[i].replace(lrword[i], '_') for i in range(0, len(lrword))}

def igame():
    system('clear')
    print('Bienvenido al juego del ahorcado')
    print('Tienes que advinar la palabra' )
    for letter in rword:
        print(letter.replace(letter, '_'), end=" ")
    print(' ')
    print(' ')

def update_write():
    global i, state, user_letter
    for i in drword:
        if user_letter == drword[i]:
            dgword.update({i: user_letter})
            for key, value in dgword.items():
                print(value, end=" ")
            print(' ') 

def detection():
    global x, user_letter
    user_letter= input('Ingresa una letra: ')
    x = rword.count(user_letter)

def mistake():
    print('Esta letra no es correcta')
    print('Te quedan ', str(lives), 'vidas. Intenta de nuevo')
    for key, value in dgword.items():
        print(value, end=" ")
    print(' ') 

def clear():
    system('clear')

def mistake():
    print('Esta letra no es correcta')
    print('Te quedan ', str(lives), 'vidas. Intenta de nuevo')
    for key, value in dgword.items():
        print(value, end=" ")
    print(' ')  

def game():
    global lives
    lives = int(5)
    igame()
    while lives != 0:
        detection()
        if x > 0:
            clear()
            update_write()
        elif x == 0:
            lives = lives - 1
            clear()
            mistake()
        if drword == dgword:
            print('Felicidades, adivinaste la palabra!!!!')
            break
        if lives == 0:
            print('Lo lamento, te quedaste sin vidas, intentalo e nuevo.')
            print('La respuesta correcta era: ')
            for key, value in drword.items():
                print(value, end=" ")
            print(' ')
            
if __name__ == '__main__':
    read()
    random_word()
    wlist()
    game()
