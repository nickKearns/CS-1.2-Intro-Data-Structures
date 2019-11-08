from flask import Flask, render_template
from cleanup import read_file
import os
from dictogram import Dictogram
from listogram import Listogram
from markov import markov_sentence, build_markov_chain
app = Flask(__name__)

@app.route('/')
def index():

    words_list = read_file('sherlock_holmes.txt')
    num_words = 10
    # histo = Dictogram(words_list)
    # sampled_sentence = ""
    chain = build_markov_chain(words_list)
    sampled_sentence = markov_sentence(chain, num_words)
    # for x in range(0, num_words):
    #   sampled_sentence += histo.sample() + " "
    return render_template('index.html', random_sentence = sampled_sentence)

if __name__ == '__main__':
  app.run(debug=True)