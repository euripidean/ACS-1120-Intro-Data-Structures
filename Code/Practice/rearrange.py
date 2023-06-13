import random
import sys

def rearrange(phrase):
    new_phrase = []
    while len(phrase) > 0:
        rand_index = random.randint(0, len(phrase) - 1)
        new_phrase.append(phrase[rand_index])
        phrase.pop(rand_index)
    return ' '.join(new_phrase)

if __name__ == '__main__':
    phrase = sys.argv[1:]
    print(rearrange(phrase))

