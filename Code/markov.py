from dictogram import Dictogram
from sample import sample_dict_hist, create_sentence
from random import choice

from cleanup import read_file
words_list = read_file('sherlock_holmes.txt')





class Markov():
    def __init__(self, words_list):
        self.chain = {}
        for index, word in enumerate(words_list):
            if word not in self.chain:
                if index < len(words_list) - 1:
                    self.chain[word] = [words_list[index+1]]
            elif word in self.chain:
                if index < len(words_list) -1:
                    self.chain[word].append(words_list[index+1])


        for key in self.chain:
            self.chain[key] = Dictogram(self.chain[key])

    def create_sentence(self, num_words):
        sampled_sentence = []
        sampled_sentence.append(choice(list(self.chain.keys())))
        for i in range(0, num_words-1):
            sampled_sentence.append(self.chain[sampled_sentence[i]].sample())
        return ' '.join(sampled_sentence)





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
    for i in range(0, length-1):
        sampled_sentence.append(chain[sampled_sentence[i]].sample())
    return ' '.join(sampled_sentence)



# print(build_markov_chain(words_list))
# print(markov_sentence(build_markov_chain(words_list), 10))
