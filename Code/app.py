from flask import Flask, render_template
from sample import sample_dict_hist, sample_hist, create_sentence
from histogram import histogram, list_histogram
app = Flask(__name__)

@app.route('/')
def index():

    histo = histogram('sherlock_holmes.txt')
    sampled_sentence = create_sentence(histo, 10)
    return render_template('index.html', random_sentence = sampled_sentence)