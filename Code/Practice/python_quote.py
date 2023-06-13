import random


quotes = ("It's just a flesh wound.",
          "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!",
          "A scratch? Your arm's off!",
          "I'm not dead!",
          "I'm getting better!",
          "I fart in your general direction.",
          "'Judean People's Front'. We're the People's Front of Judea!",
          "I'm Brian and so's my wife!")


def random_python_quote():
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]

if __name__ == '__main__':
    quote = random_python_quote()
    print(quote)
