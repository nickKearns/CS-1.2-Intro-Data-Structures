import random, sys

def rearrange_words(words):
    temp_arr = []
    indices_used = []
    for x in range(len(words)):
        temp_word = random.choice(words)
        temp_arr.append(temp_word)
        words.remove(temp_word)
    return temp_arr



if __name__ == '__main__':
    words = sys.argv[1:]
    print(rearrange_words(words))