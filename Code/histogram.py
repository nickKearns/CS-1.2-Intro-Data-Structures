import sys
import re
from cleanup import read_file



def histogram(source_text):
    '''
        a function to take a text file and log each word and its frequency into a dictionary histogram

        input: the text file to be processed

        output: a dictionary histogram
    '''
    words_list = read_file(source_text)
    histogram = {}
    

    for word in words_list:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1

    return histogram


def histogram_from_string(words_string):
    '''
        a function that creates a dictionary histogram from an inputed string

        input: a string to be processed

        output: a dictionary histogram
    '''

    histogram = {}
    words_list = words_string.split()

    for word in words_list:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram




def list_histogram(source_text):
    '''
        a function to take a text file and log each word and its frequency into a list of lists histogram

        input: the text file to be processed

        output: a list of lists histogram
    '''


    histogram = []
    words_list = read_file(source_text)

    for word in words_list:
        tmp_list = [word, 1]
        found_word = False
        found_word_index = None
        for index, value in enumerate(histogram):
            if value[0] == tmp_list[0]:
                found_word = True
                found_word_index = index
        if found_word:
            # increment
            histogram[found_word_index][1] += 1
        else:
            # append temp list
            histogram.append(tmp_list)
        found_word = False
        found_word_index = None
                
    return histogram




def tuple_histogram(source_text):
    '''
        a function to take a text file and log each word and its frequency into a list of tuples histogram

        input: the text file to be processed

        output: a list of tuples histogram
    '''

    histogram = []
    words_list = read_file(source_text)

    for word in words_list:
        tmp_tuple = (word, 1)
        found_word = False
        found_index = None
        for index, value in enumerate(histogram):
            if value[0] == tmp_tuple[0]:
                new_num_occ = histogram[index][1]
                new_num_occ += 1
                new_tuple = (word, new_num_occ)
                found_word = True
                found_index = index
        if found_word:
            histogram[found_index] = new_tuple
        else:
            histogram.append(tmp_tuple)
        found_word = False
        found_index = None
    return histogram







def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    return histogram[word]







if __name__ == '__main__':
    source_text = sys.argv[1]
    # print(list_histogram(source_text))
    # print(tuple_histogram(source_text))
    # print(unique_words(histogram(source_text)))
    # print(frequency('fish', histogram(source_text)))
    print(histogram(source_text))
    # print(list_histogram(source_text))
    # print(tuple_histogram(source_text))
