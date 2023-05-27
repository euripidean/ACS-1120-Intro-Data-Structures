import sys
import random

# read in system words file
def read_words():
    with open('/usr/share/dict/words', 'r') as f:
        words = f.read().splitlines()
    return words

# takes in the number of words from the system as an argument, then runs the read_words function and generates a sentence of that many words
def generate_sentence(num_words):
    words = read_words()
    sentence = []
    for i in range(int(num_words)):
        sentence.append(words[random.randint(0, len(words))])
    sentence = [word.lower() for word in sentence]
    sentence[0] = sentence[0].capitalize()
    sentence[-1] = sentence[-1] + '.'
    return ' '.join(sentence)
    

if __name__ == '__main__': 
    print(generate_sentence(sys.argv[1]))
