import random
import sys
from histogram import histogram, histogram_from_string


def sample(histo):
        upper_bound = sum(histo.values())
        ran_num = random.randint(1, upper_bound)
        # print(ran_num)
        total = 0
        for key, value in histo.items():
                total += value
                if total >= ran_num:
                        return key



def sample_test(source_text, num_iterations):   
        histo = histogram(source_text)
        outputs = []
        for x in range(num_iterations):
                outputs.append(sample(histo))
                # print(outputs)
        return histogram_from_string(' '.join(outputs))




if __name__ == '__main__':
    source_text = sys.argv[1]
    histo = histogram(source_text)
    print(sample(histo))

#     sample_data_string = sample_test(source_text, 50)
    data_histo = sample_test(source_text, 100)
    print(data_histo)





