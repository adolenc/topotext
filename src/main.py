from preprocessor import Preprocessor
from prepreprocessor import Prepreprocessor
from features_funcs import word_lengths_funcs, sentence_lengths_funcs, ratio_most_n_common_words, \
    ratio_length_of_words_texts
from operator import ge
from utils import flatten,get_groups,halve_group,get_max_dist
from cech import cech
from alpha_shapes import alpha_shapes
from persistence_diagrams import persistence_diagram,fix_infs
from clustering import cluster_distances
from dionysus import PersistenceDiagram
from draw import draw_bar_code_graph,draw_persistance_diagram


funcs = [word_lengths_funcs, sentence_lengths_funcs, ratio_most_n_common_words, ratio_length_of_words_texts,
            lambda text: ratio_length_of_words_texts(text, 8, ge)]
pp = Preprocessor(Prepreprocessor, funcs, use_tfidf=20)
folder_names = ['abstracts', 'sports', 'reviews']
X, y = pp.process(['../data/' + fold_n for fold_n in folder_names])
Xs = flatten(map(halve_group, get_groups(X, y)))
Rs = map(get_max_dist, Xs)
cxs = map(alpha_shapes, Xs)
diagrams = [persistence_diagram(cx, R) for cx, R in zip(cxs, Rs)]
titles = flatten([[name + '_train', name + '_test'] for name in folder_names])
cluster_distances(map(lambda diagram: [PersistenceDiagram(d, diagram[d]) for d in range(3)], diagrams),
                  ps=[0,1,2], labels=titles, name="main")
i = 0
for diagram in diagrams:
    diagram, max_j = fix_infs(diagram)
    draw_persistance_diagram(diagram, max_j, titles[i])
    draw_bar_code_graph(diagram, max_j, titles[i])
    i += 1
