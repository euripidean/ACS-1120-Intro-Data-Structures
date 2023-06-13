from histogram import histogram
import random

source_text = './Text/FrankensteinExtract.txt'

def weighted_sample():
    words = histogram(source_text)
    weighted_words = []
    # for each word in the histogram, add it to the list as many times as the count of that word
    for word in words:
        for i in range(words[word]):
            weighted_words.append(word)
    # return a random word from the list
    return random.choice(weighted_words)

def gpt_weighted_sample():
    words = histogram(source_text)
    weighted_words = [word for word in words for _ in range(words[word])]
    return random.choice(weighted_words)

def weighted_sample_tuple():
    words = histogram(source_text)
    weighted_words = []
    for word, count in words.items():
        weighted_words.extend([word] * count)
    return random.choice(weighted_words)
    
def show_likelihood():
    words = histogram(source_text)
    likelihood = {}
    for word in words:
        #truncate to 2 decimal places
        likelihood[word] = round(words[word] / len(words), 4)
    # sort likelihood descending by value and keep the top 100
    likelihood = dict(sorted(likelihood.items(), key=lambda item: item[1], reverse=True)[:100])
    return likelihood




if __name__ == '__main__':
   print(show_likelihood())
   print(weighted_sample())
