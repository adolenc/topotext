from preprocessor import Preprocessor
from prepreprocessor import Prepreprocessor
from features_funcs import word_lengths_funcs, sentence_lengths_funcs, ratio_most_n_common_words, \
    ratio_length_of_words_texts
from operator import ge
from sklearn.cluster import SpectralClustering,KMeans
from sklearn.metrics import adjusted_rand_score,mutual_info_score
from sklearn.decomposition import PCA
import scipy.spatial.distance as ssd
from scipy.cluster.hierarchy import linkage, fcluster
from dionysus import PairwiseDistances,ExplicitDistances
import numpy as np

def bench_cluster(X, y, pca_n_comp):
    n = len(np.unique(y))
    pca = PCA(pca_n_comp)
    X_ = pca.fit_transform(X)
    sc = SpectralClustering(n)
    km = KMeans(n)
    sc_pred = sc.fit_predict(X_)
    km_pred = km.fit_predict(X_)
    distances = PairwiseDistances(X_.tolist())
    distances = ExplicitDistances(distances)
    singlel_pred = fcluster(linkage(ssd.squareform(distances.distances)), n, criterion='maxclust')
    print "single-linkage clustering prediction:", singlel_pred
    print "single-linkage clustering score:", adjusted_rand_score(y, singlel_pred), mutual_info_score(y, singlel_pred)
    print "spectral clustering prediction:", sc_pred
    print "spectral clustering score:", adjusted_rand_score(y, sc_pred), mutual_info_score(y, sc_pred)
    print "kmeans clustering prediction", km_pred
    print "kmeans clustering score:", adjusted_rand_score(y, km_pred), mutual_info_score(y, km_pred)
    print "ground truth labels", y


if __name__ == "__main__":
    funcs = [word_lengths_funcs, sentence_lengths_funcs, ratio_most_n_common_words, ratio_length_of_words_texts,
            lambda text: ratio_length_of_words_texts(text, 8, ge)]
    pp = Preprocessor(Prepreprocessor, funcs, use_tfidf=20)
    X, y = pp.process(['../data/abstracts/', '../data/sports', '../data/reviews'])
    bench_cluster(X, y, 3)
