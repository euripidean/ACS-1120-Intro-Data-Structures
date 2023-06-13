import sys
import random

def read_words():
    with open('/usr/share/dict/words', 'r') as f:
        words = f.read().splitlines()
    return words

def prompt():
    # user enters the beginning of a word and the program returns a list of possible words that begin with that string
    user_input = input('Enter the beginning of a word: ')
    while len(user_input) < 2 or user_input.isalpha() == False:
        user_input = input('Input error. Enter the beginning of a word: ')
    return user_input

def autocomplete(user_input):
    words = read_words()
    possible_words = []
    for word in words:
        if word.startswith(user_input):
            possible_words.append(word)
    if len(possible_words) == 0:
        print('No words found.')
        sys.exit()
    print('Here are your possible words:')
    for word in possible_words:
        print(word)

if __name__ == '__main__':
    user_input = prompt()
    autocomplete(user_input)
        
