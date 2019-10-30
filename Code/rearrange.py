import random, sys

def rearrange_words(words):
    temp_list = []
    indices_used = []
    for x in range(len(words)):
        temp_word = random.choice(words)
        temp_list.append(temp_word)
        words.remove(temp_word)
    return temp_list



if __name__ == '__main__':
    words = sys.argv[1:]
    print(rearrange_words(words))