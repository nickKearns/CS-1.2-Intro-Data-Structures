from rearrange import rearrange_words
import sys
import random
def dictionary_words(num_words):
    with open("/usr/share/dict/words") as f:
        random_sentence = []
        dict_list = f.readlines()
        count = 0
        while count < int(num_words):
            rand_index = random.randint(0, len(dict_list) - 1)
            random_sentence.append(dict_list[rand_index].strip())
            count += 1
    return ' '.join(random_sentence)


        





if __name__ == '__main__':
    num_words = int(sys.argv[1])
    sample_sentence = dictionary_words(num_words)
    print(sample_sentence)
    

