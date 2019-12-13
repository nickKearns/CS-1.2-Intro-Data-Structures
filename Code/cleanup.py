import re
def read_file(source_text):
    with open (source_text, 'r') as f:
        words = f.read()
        words_list = re.sub(r'[^a-zA-Z\s]', '', words).lower()
        # words_list = words_list.replace(" am ", "")
        # words_list = words_list.replace(" pm ", "")
        word_list = words_list.split()
    return word_list
