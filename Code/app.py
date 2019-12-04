from flask import Flask, render_template, request
from cleanup import read_file
import os
from dictogram import Dictogram
from listogram import Listogram
from markov import Markov
app = Flask(__name__)

@app.route('/')
def index():

    words_list = read_file('seinfeld.txt')
    num_words = int(request.args.get('num_words', 10))
    chain = Markov(words_list)
    sampled_sentence = chain.create_sentence(num_words)
    return render_template('index.html', random_sentence = sampled_sentence, num_words=num_words)

if __name__ == '__main__':
  app.run(debug=True)