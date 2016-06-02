from preprocessor import Preprocessor
from prepreprocessor import Prepreprocessor
from features_funcs import word_lengths_funcs, sentence_lengths_funcs, ratio_most_n_common_words, \
    ratio_length_of_words_texts
from operator import ge
from sklearn.cluster import SpectralClustering,KMeans
from sklearn.metrics import adjusted_rand_score,mutual_info_score

if __name__ == "__main__":
    funcs = [word_lengths_funcs, sentence_lengths_funcs, ratio_most_n_common_words, ratio_length_of_words_texts,
            lambda text: ratio_length_of_words_texts(text, 8, ge)]
    pp = Preprocessor(Prepreprocessor, funcs, use_tfidf=20)
    X, y = pp.process(['../data/abstracts/', '../data/sports', '../data/reviews'])
    sc = SpectralClustering(3)
    km = KMeans(3)
    sc_pred = sc.fit_predict(X)
    km_pred = km.fit_predict(X)
    print "spectral clustering prediction:", sc_pred
    print "spectral clustering score:", adjusted_rand_score(y, sc_pred), mutual_info_score(y, sc_pred)
    print "kmeans clustering prediction", km_pred
    print "kmeans clustering score:", adjusted_rand_score(y, km_pred), mutual_info_score(y, km_pred)
    print "ground truth labels", y
