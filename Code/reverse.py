import sys

def reverse(phrase):
    if not phrase:
        return "Provide a string to reverse."
    if len(phrase) == 1:
        phrase = phrase[0]
        phrase = list(phrase)
        phrase.reverse()
        return ''.join(phrase)
    else:
        phrase.reverse()
    return ' '.join(phrase)

if __name__ == '__main__':
    phrase = sys.argv[1:]
    print(reverse(phrase))
