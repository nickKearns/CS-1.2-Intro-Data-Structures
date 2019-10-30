import sys




def histogram(source_text):
    with open (source_text) as f:
        histogram = {}
        words = f.read()
        words_list = words.split()

        for word in words_list:
            if word in histogram:
                histogram[word] += 1
            else:
                histogram[word] = 1

    return histogram

def unique_words(histogram):
    return len(histogram)

def frequency(word, histogram):
    return histogram[word]



def list_histogram(source_text):
    with open (source_text) as f:
        histogram = []
        words = f.read()
        words_list = words.split()
        print(words_list)
        first_word = [words_list[0], 1]
        print(first_word)
        histogram.append(first_word)
        for x in range(len(histogram)):
            for word in words_list:
                temp_list = [word, 1]
                if temp_list in histogram:
                    histogram[x][1] += 1
                else:
                    histogram.append(temp_list)


    return histogram





if __name__ == '__main__':
    source_text = sys.argv[1]
    print(list_histogram(source_text))
    # print(unique_words(histogram(source_text)))
    # print(frequency('fish', histogram(source_text)))
