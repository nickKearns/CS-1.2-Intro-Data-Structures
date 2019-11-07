from flask import Flask, render_template
from cleanup import read_file
from sample import sample_dict_hist, sample_hist, create_sentence
from histogram import histogram, list_histogram
import os
from dictogram import Dictogram
from listogram import Listogram
app = Flask(__name__)

@app.route('/')
def index():

    words_list = read_file('sherlock_holmes.txt')
    num_words = 10
    histo = Dictogram(words_list)
    sampled_sentence = ""
    for x in range(0, num_words):
      sampled_sentence += histo.sample() + " "
    return render_template('index.html', random_sentence = sampled_sentence)

if __name__ == '__main__':
  app.run(debug=True)