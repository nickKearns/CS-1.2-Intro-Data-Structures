import random
import sys
from histogram import histogram, histogram_from_string, list_histogram, tuple_histogram


def sample_dict_hist(histo):
        '''
                function to randomly select a word from a histogram based on the number of times it occurs WORKS FOR DICTIONARIES

                input: the histogram to be processed

                output: returns a word based on its weighted probability
        '''

        upper_bound = sum(histo.values())
        ran_num = random.randint(1, upper_bound)
        # print(ran_num)
        total = 0
        for key, value in histo.items():
                total += value
                if total >= ran_num:
                        return key



def sample_hist(histo):
        '''
                function to randomly select a word from a histogram based on the number of times it occurs WORKS FOR LIST OF LISTS OR LIST OF TUPLES

                input: the histogram to be processed

                output: returns a word based on its weighted probability
        '''



        upper_bound = 0
        for outer_index in range(len(histo)):
                upper_bound += histo[outer_index][1]
        
                
        ran_num = random.randint(1, upper_bound)

        total = 0
        for outer_index in range(len(histo)):
                total += histo[outer_index][1]
                if total >= ran_num:
                        return histo[outer_index][0]




def sample_test_dict(source_text, num_iterations):   
        '''
                function to test the accuracy of weighted probability, words for dictionary histograms

                input: the text file to be read and the number of iterations to be run
                
                output: a histogram that displays each word and the number of times they were randomly selected
        '''

        histo = histogram(source_text)
        outputs = []
        for x in range(num_iterations):
                outputs.append(sample_hist(histo))
                # print(outputs)
        return histogram_from_string(' '.join(outputs))


def sample_test_hist(source_text, num_iterations):  
        '''
                function to test the accuracy of weighted probability, works for list of lists histogram and list of tuples histogram

                input: the text file to be read and the number of iterations to be run

                output: a histogram that displays each word and the number of times they were randomly selected
        '''

        histo = tuple_histogram(source_text)
        outputs = []
        for x in range(num_iterations):
                outputs.append(sample_hist(histo))
                # print(outputs)
        return histogram_from_string(' '.join(outputs))


if __name__ == '__main__':
        source_text = sys.argv[1]
        histo = histogram(source_text)
        # histo = list_histogram(source_text)
        # print(sample_dict_hist(histo))

#     sample_data_string = sample_test(source_text, 50)
        data_histo = sample_test_hist(source_text, 100)


        print(data_histo)





