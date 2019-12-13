from dictogram import Dictogram
from sample import sample_dict_hist, create_sentence
from random import choice

from cleanup import read_file





class Markov():
    def __init__(self, words_list):
        self.chain = {}
        for index, prev_word in enumerate(words_list):
            # Skip the last 2 words in the list
            if index < len(words_list) - 2:
                curr_word = words_list[index+1]
                # Create a pair of this prev_word and the next word
                word_pair = (prev_word, curr_word)
                # If we haven't seen these words before, make an empty histogram
                if word_pair not in self.chain:
                        self.chain[word_pair] = Dictogram()
                # Add a new entry to the histgram for these words (this state)
                next_word = words_list[index+2]
                self.chain[word_pair].add_count(next_word)


    def create_sentence(self, num_words):
        sampled_tuple = ()
        sampled_words = []
        # Choose a starting state uniformly at random
        sampled_tuple = choice(list(self.chain.keys()))

        #add the first word pair chosen to the sampled words
        sampled_words.extend(sampled_tuple)

        # start at 0 and stop at len - 2 because it will try and sample beyond the range if not
        for i in range(0, num_words - 2):
            # sample a new word based on the current word pair
            sampled_word = self.chain[sampled_tuple].sample() 
            sampled_words.append(sampled_word)
            #set second word to be the current word pair's second word
            second_word = sampled_tuple[1]
            # set new tuple to be the second word from the previous tuple and the new sampled word
            new_tuple = (second_word, sampled_word)
            #set sampled tuple to be the new tuple
            sampled_tuple = new_tuple

        finished_sentence = ' '.join(sampled_words)
        return finished_sentence





# def build_markov_chain(words_list):
#     markov = {}
#     for index, word in enumerate(words_list):
#         if word not in markov:
#             if index < len(words_list) - 1:
#                 markov[word] = [words_list[index+1]]
#         elif word in markov:
#             if index < len(words_list) -1:
#                 markov[word].append(words_list[index+1])


#     for key in markov:
#         markov[key] = Dictogram(markov[key])
#     return markov

# def markov_sentence(chain, length):
#     sampled_sentence = []
#     sampled_sentence.append(choice(list(chain.keys())))
#     for i in range(0, length-1):
#         sampled_sentence.append(chain[sampled_sentence[i]].sample())
#     return ' '.join(sampled_sentence)



# print(build_markov_chain(words_list))
# print(markov_sentence(build_markov_chain(words_list), 10))


if __name__ == "__main__":
    words_list = read_file('sherlock_holmes.txt')
    test_markov_chain = Markov(words_list)
    markov_sentence = test_markov_chain.create_sentence(15)
    print(markov_sentence)
