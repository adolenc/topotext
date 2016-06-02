from preprocessor import Preprocessor
from prepreprocessor import Prepreprocessor
from features_funcs import word_lengths_funcs, sentence_lengths_funcs, ratio_most_n_common_words, \
    ratio_length_of_words_texts
from operator import ge
from utils import flatten,get_groups,halve_group,get_max_dist
from cech import cech
from alpha_shapes import alpha_shapes
from persistence_diagrams import persistence_diagram
from clustering import cluster_distances
from dionysus import PersistenceDiagram


funcs = [word_lengths_funcs, sentence_lengths_funcs, ratio_most_n_common_words, ratio_length_of_words_texts,
            lambda text: ratio_length_of_words_texts(text, 8, ge)]
pp = Preprocessor(Prepreprocessor, funcs, use_tfidf=3)
X, y = pp.process(['../data/abstracts/', '../data/sports', '../data/reviews'])
Xs = flatten(map(halve_group, get_groups(X, y)))
Rs = map(get_max_dist, Xs)
print Rs
cxs = map(cech, Xs)
diagrams = [persistence_diagram(cx, R) for cx, R in zip(cxs, Rs)]
cluster_distances(map(lambda diagram: [PersistenceDiagram(d, diagram[d]) for d in range(3)], diagrams))
