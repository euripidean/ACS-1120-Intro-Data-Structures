import sys
import random

source_text = './Code/Text/FrankensteinExtract.txt'

# Read Frankenstein from the file and put into dictionary, counting the number of times each word appears
def histogram(source_text):
    with open(source_text, 'r') as f:
        frankenstein = f.read()
        frankenstein = frankenstein.split()
        f.close()
        histogram = {}
        for word in frankenstein:
            if word in histogram:
                histogram[word] += 1
            else:
                histogram[word] = 1
        return histogram
    

# Return the number of unique words in the histogram
def unique_words(histogram):
    print(histogram)
    print('The number of unique words in the histogram is:')
    return len(histogram)

def prompt_user():
    user_word = input("Enter a word to find its frequency: ")
    if not user_word.isalpha():
        user_word = input("Enter a valid word to find its frequency: ")
    return user_word

# Return the frequency of a given word
def frequency(word, histogram = histogram(source_text)):
    if word not in histogram:
        return "Word not found."
    else:
        return histogram[word]


    

# if main
if __name__ == '__main__':
    histogram = histogram(source_text)
    print(unique_words(histogram))
    word = prompt_user()
    print(frequency(word, histogram))
    
