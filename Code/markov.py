from dictogram import Dictogram
from sample import sample_dict_hist, create_sentence
from random import choice

from cleanup import read_file
words_list = read_file('sherlock_holmes.txt')

def build_markov_chain(words_list):
    markov = {}
    for index, word in enumerate(words_list):
        if word not in markov:
            if index < len(words_list) - 1:
                markov[word] = [words_list[index+1]]
        elif word in markov:
            if index < len(words_list) -1:
                markov[word].append(words_list[index+1])


    for key in markov:
        markov[key] = Dictogram(markov[key])
    return markov


def markov_sentence(chain, length):
    sampled_sentence = []
    sampled_sentence.append(choice(list(chain.keys())))
    for i in range(length):
        sampled_sentence.append(chain[sampled_sentence[i]].sample())
    return ' '.join(sampled_sentence)



# print(build_markov_chain(words_list))
# print(markov_sentence(build_markov_chain(words_list), 10))
