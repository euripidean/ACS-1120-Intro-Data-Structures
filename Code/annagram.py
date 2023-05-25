import random
import sys

def annagram(word):
    if not word:
        return "Provide a word to annagram."
    if len(word) > 1:
        return "Provide a single word to annagram"
    else:
        word = word[0]
        word = list(word)
        if len(word) > 3:
            random.shuffle(word)
            return ''.join(word)
        else:
            return "Word must be longer than 3 characters."
    

if __name__ == '__main__':
    word = sys.argv[1:]
    print(annagram(word))
