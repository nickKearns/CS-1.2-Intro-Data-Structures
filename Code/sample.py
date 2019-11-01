import random
import sys
from histogram import histogram


def sample(source_text):
    hist = histogram(source_text)
    upper_bound = 0
    for value in hist.values():
        upper_bound += value
    ran_num = random.randint(1, upper_bound)
    total = 1
    for key, value in hist.items():
        total += value
        if total >= ran_num:
            return key








if __name__ == '__main__':
    source_text = sys.argv[1]
    histo = histogram(source_text)
    print(sample(source_text))





