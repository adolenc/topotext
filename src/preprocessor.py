import numpy as np
from tf_idf import *
from utils import flatten,load_directory,write_matrix, map_flatten
from prepreprocessor import *
from features_funcs import word_lengths_funcs, sentence_lengths_funcs, ratio_most_n_common_words, \
    ratio_length_of_words_texts
from operator import ge

class Preprocessor():
    """Preprocess datasets into an matrix of samples/features.

    Parameters
    ----------
    prepreprocessor: callable which gets called with a string representing each
        individual text and should return a list of words.

    feature_funs: a list of functions which should take a list of
        prepreprocessed words as an input and return a list of values
        representing features.

    use_tfidf: False or a natural number representing number of tf/idf features
        to take.
    """
    def __init__(self, prepreprocessor, feature_funs, use_tfidf=False):
        self.prepreprocessor_ = prepreprocessor
        self.feature_funs_ = feature_funs
        self.use_tfidf_ = use_tfidf

    def process(self, datasets):
        """ Take a list of directories (each directory with text files
        representing a separate class) and return resulting X and y matrices,
        calculated by applying prepreprocessor, feature_funs and optionally
        tf/idf.
        """
        texts = map(load_directory, datasets)
        y = flatten([[n] * len(d) for n, d in enumerate(texts)])
        pp_texts = map(self.prepreprocessor_, flatten(texts))
        X = [np.array(f(pp_texts)) for f in self.feature_funs_]
        X = [x.reshape(-1,1) if len(np.shape(x)) == 1 else x for x in X]
        if list(X):
            X = np.hstack(X)
        if self.use_tfidf_:
            words = get_words(map_flatten(pp_texts), self.use_tfidf_)
            M = get_M(map_flatten(pp_texts), words)
            tf_idf = get_tf_idf_M(M) # generate self.use_tfidf_ number of new features
            if list(X):
                X = np.hstack((X, tf_idf)) # glue them to X
            else:
                X = tf_idf
        return np.array(X), np.array(y)


if __name__ == '__main__':
    funcs = [word_lengths_funcs, sentence_lengths_funcs, ratio_most_n_common_words, ratio_length_of_words_texts,
                lambda text: ratio_length_of_words_texts(text, 8, ge)]
    pp = Preprocessor(Prepreprocessor, funcs, use_tfidf=3)
    X, y = pp.process(['../data/abstracts/', '../data/abstracts'])
    print X.shape
    print X
    write_matrix(X, "test.mat")
