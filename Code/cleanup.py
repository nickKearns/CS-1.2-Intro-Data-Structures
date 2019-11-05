import re
def read_file(source_text):
    with open (source_text, 'r') as f:
        words = f.read()
        # words_list = re.sub(r'[^a-zA-Z\s]', '', words)
        words_list = re.sub(r'[^a-zA-Z\s]', '', words)
        word_list = words_list.split()
    return word_list
