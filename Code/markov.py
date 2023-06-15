# // markov class extends dictogram class

import random
from dictogram import Dictogram


class Markov(Dictogram):
    """Markov chain that uses a dictionary histogram to store word counts."""
    
    def __init__(self, word_list=None):
        """Initialize this histogram as a new dict and count given words."""
        super(Markov, self).__init__()  # Initialize this as a new dict
        self.types = 0
        self.tokens = 0
        self.word_list = word_list
        self.markov_dict = {}
        self.markov_dict = self.markov_chain()

    def markov_chain(self):
        """Create a Markov chain from given data string."""
        for index in range(len(self.word_list)):
            word = self.word_list[index]
            if index < len(self.word_list) - 1:
                next_word = self.word_list[index + 1]
            else:
                next_word = None
            next_word_dict = self.markov_dict.get(word, Dictogram())
            if next_word:
                next_word_dict.add_count(next_word)
            self.markov_dict[word] = next_word_dict
        return self.markov_dict
    
    def random_walk(self, num_words=10):
        """Randomly walk the markov chain and return a list of words."""
        sentence = []
        word = random.choice(self.word_list)
        for _ in range(num_words):
            sentence.append(word)
            word = self.markov_dict[word].sample()
        return sentence
    
    def print_markov_chain(self, num_samples=10):
        """Print a sample of the Markov chain."""
        print('Markov chain samples:')
        for _ in range(num_samples):
            sentence = self.random_walk()
            print(' '.join(sentence))
        print()

def main():
    # Sample text as an explicitly stated variable
    sample_text = """You will rejoice to hear that no disaster has accompanied the
commencement of an enterprise which you have regarded with such evil
forebodings I arrived here yesterday, and my first task is to assure
my dear sister of my welfare and increasing confidence in the success
of my undertaking"""

    word_list = sample_text.split()
    markov = Markov(word_list)
    markov.print_markov_chain()
    print("Random Sentence:", ' '.join(markov.random_walk()))

if __name__ == '__main__':
    main()
