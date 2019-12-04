from dictogram import Dictogram
from sample import sample_dict_hist, create_sentence
from random import choice

from cleanup import read_file
words_list = read_file('sherlock_holmes.txt')





class Markov():
    def __init__(self, words_list):
        self.chain = {}
        for index, word in enumerate(words_list):
            if index < len(words_list) - 2:
                tmp_tuple = (word, words_list[index+1])
            if tmp_tuple not in self.chain:
                if index < len(words_list) - 2:
                    self.chain[tmp_tuple] = [words_list[index+2]]
            elif tmp_tuple in self.chain:
                if index < len(words_list) - 2:
                    self.chain[tmp_tuple].append(words_list[index+2])


        for key in self.chain:
            self.chain[key] = Dictogram(self.chain[key])

    def create_sentence(self, num_words):
        sampled_sentence = []
        finished_sentence = []
        sampled_tuple = choice(list(self.chain.keys()))
        finished_sentence.append(sampled_tuple[0])
        finished_sentence.append(sampled_tuple[1])
        # print(sampled_tuple)
        sampled_sentence.append(sampled_tuple)
        # print(sampled_sentence)
        # print(sampled_sentence[0])
        # print(sampled_sentence[0])
        for i in range(0, num_words - 2):
            
            sampled_word = self.chain[sampled_sentence[i]].sample() #sampled tuple will change to tuple at index i
            # print(sampled_word)
            second_word = sampled_sentence[i][1]
            # print(second_word)
            new_tuple = (second_word, sampled_word)
            # print(new_tuple)
            next_word = self.chain[new_tuple].sample()
            # print(next_word)
            finished_sentence.append(sampled_word)
            sampled_sentence.append(new_tuple)
            # print(sampled_sentence)

            # get_next_word = (sampled_sentence[i], self.chain[(sampled_tuple[1], self.chain[sampled_tuple].sample())])
            # sampled_sentence.append(get_next_word)
        print(sampled_sentence)
        return ' '.join(finished_sentence)





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
    test_markov_chain = Markov(words_list)
    print(test_markov_chain.chain)
    markov_sentence = test_markov_chain.create_sentence(15)
    print(markov_sentence)
