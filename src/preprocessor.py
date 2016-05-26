import numpy as np
from utils import flatten,load_directory


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
        texts = flatten(map(load_directory, datasets))
        pp_texts = map(self.prepreprocessor_, texts)
        X = np.array([flatten([f(text) for f in self.feature_funs_]) for text in pp_texts])
        if self.use_tfidf_:
            # TODO: pass pp_texts to tfidf to generate self.use_tfidf_ number
            # of new features and glue them to X
            pass
        y = flatten([[n] * len(d) for n, d in enumerate(datasets)])
        return np.array(X), np.array(y)


if __name__ == '__main__':
    pp = Preprocessor(lambda x: x, [lambda ws: [len(ws)], lambda ws: [len(ws)/100.0]], use_tfidf=100)
    print pp.process(['../data/abstracts/', '../data/abstracts'])
