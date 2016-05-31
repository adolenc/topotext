from nltk.tokenize import RegexpTokenizer
import os
from utils import *
import numpy as np

def count_words(folder_path):
    tokenizer = RegexpTokenizer(r'\w+')
    lengths = []
    for filename in os.listdir(folder_path):
        abs_path = os.path.join(folder_path, filename)
        text = read_file(abs_path)
        text_len = len(tokenizer.tokenize(text))
        lengths.append([str(abs_path), text_len])
    return np.array(lengths)

if __name__ == '__main__':
    sports = count_words("../data/abstracts")
    abstracts = count_words("../data/sports")
    print sports
    print abstracts
