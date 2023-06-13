from histogram import histogram
import random

source_text = './Code/Text/FrankensteinExtract.txt'

# get a random word from the histogram
def sample():
    words = histogram(source_text)
    word = random.choice(list(words.keys()))
    return word

# if main
if __name__ == '__main__':
    print(sample())
    