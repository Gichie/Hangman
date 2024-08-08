import sys
import time
from random import choice


def sleeping():
    time.sleep(0.3)


def display_hangman(tries):
    hangman = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
          /-\\
        ****YOU DIED!!!
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return hangman[tries]


def choose_word():
    with open('words.txt', encoding='utf-8') as file:
        return choice([word.strip() for word in file]).upper()


def victory():
    print(f'''                                           
★░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░★
★░░░░░░░░░███░██░░░░░░░░░░░░░░░░░░░░★
★░░░░░░░░░██░░░█░░░░░░░░░░░░░░░░░░░░★
★░░░░░░░░░██░░░██░░░░░░░░░░░░░░░░░░░★
★░░░░░░░░░░██░░░███░░░░░░░░░░░░░░░░░★
★░░░░░░░░░░░██░░░░██░░░░░░░░░░░░░░░░★
★░░░░░░░░░░░██░░░░░███░░░░░░░░░░░░░░★
★░░░░░░░░░░░░██░░░░░░██░░░░░░░░░░░░░★
★░░░░░░░███████░░░░░░░██░░░░░░░░░░░░★
★░░░░█████░░░░░░░░░░░░░░███░██░░░░░░★
★░░░██░░░░░████░░░░░░░░░░██████░░░░░★
★░░░██░░████░░███░░░░░░░░░░░░░██░░░░★
★░░░██░░░░░░░░███░░░░░░░░░░░░░██░░░░★
★░░░░██████████░███░░░░░░░░░░░██░░░░★
★░░░░██░░░░░░░░████░░░░░░░░░░░██░░░░★
★░░░░███████████░░██░░░░░░░░░░██░░░░★
★░░░░░░██░░░░░░░████░░░░░██████░░░░░★
★░░░░░░██████████░██░░░░███░██░░░░░░★
★░░░░░░░░░██░░░░░████░███░░░░░░░░░░░★
★░░░░░░░░░█████████████░░░░░░░░░░░░░★
★░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░★''')
    sleeping()
    print('Поздравляю, вы отгадали слово и остались живы!')
    sleeping()
    check_new_game()


def lose(hidden_word):
    sleeping()
    print(f'Это было слово: {hidden_word}')
    print(f''' 
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████''')
    sleeping()
    check_new_game()


def count_tries(tries):
    if tries == 1:
        print(f'Осталась {tries} попытка!')
        return None
    if tries == 2 or tries == 3 or tries == 4:
        print(f'Осталось {tries} попытки')
    if tries == 5 or tries == 6:
        print(f'Осталось {tries} попыток')


def names_letter(hidden_word, guessed_word, tries, named_letters=[]):
    while True:
        letter = input('И это буква? ').upper()
        if letter in named_letters:
            print('Эта буква уже называлась...')
            sleeping()
            print('Использованные буквы: ', ', '.join(set(named_letters)))
        else:
            if len(letter) == 1 and letter in 'абвгдежзийклмнопрстуфхцчшщъыьэюя'.upper():
                named_letters.append(letter)
                if letter in hidden_word:
                    print(f'Правильно! Откройте букву: {letter}')
                    guessed_word = ''
                    for letter in hidden_word:
                        if letter in named_letters:
                            guessed_word += letter
                            print(letter, end='')
                        else:
                            guessed_word += '-'
                            print('_', end='')
                    print()
                    if guessed_word == hidden_word:
                        return victory()
                    return choose_letter_or_word(hidden_word, guessed_word, tries)
                else:
                    print(display_hangman(tries))
                    tries -= 1
                    if tries < 0:
                        return lose(hidden_word)
                    print('Нет такой буквы')
                    sleeping()
                    print(guessed_word)
                    sleeping()
                    print('Использованные буквы: ', ', '.join(set(named_letters)))
                    sleeping()
                    count_tries(tries + 1)
                    sleeping()
            else:
                print('Такой символ неприемлем, назовите другой')


def names_word(hidden_word, guessed_word, tries):
    word = input('И это слово? ').upper()
    if word == hidden_word:
        return victory()
    else:
        print(display_hangman(tries))
        sleeping()
        tries -= 1
        if tries < 0:
            return lose(hidden_word)
        print('НЕВЕРНО!!!')
        sleeping()
        count_tries(tries + 1)
        sleeping()
        print(guessed_word)
        sleeping()
        return choose_letter_or_word(hidden_word, guessed_word, tries)


def choose_letter_or_word(hidden_word, guessed_word, tries):
    sleeping()
    while True:
        res = input('Назовете слово или букву (с / б)? ').lower()
        if res == 'б' or res == ',':
            return names_letter(hidden_word, guessed_word, tries)
        elif res == 'с' or res == 'c':
            return names_word(hidden_word, guessed_word, tries)
        else:
            print('Я тебя не понимаю, повтори ответ')
            sleeping()


def new_gamee():
    tries = 6
    hidden_word = choose_word()
    guessed_word = f"Загаданное слово: {len(hidden_word) * '_'} из {len(hidden_word)} букв"
    print(guessed_word)
    sleeping()
    print(display_hangman(tries))
    tries -= 1
    sleeping()
    return choose_letter_or_word(hidden_word, guessed_word, tries)


def check_new_game():
    while True:
        new_game = input('Начать новую игру или выйти (н / в)? ').lower()
        if new_game == 'в' or new_game == 'd':
            sys.exit()
        elif new_game == 'н' or new_game == 'y':
            sleeping()
            print('Новая игра')
            sleeping()
            return new_gamee()
        else:
            print('Вы ввели неправильное значение')


print('Это захватывающая игра Виселица. Я загадаю слово (существительное в именительном падеже, но это не точно), а ты попробуешь отгадать его за 6 попыток.')
print()
check_new_game()
