from utils import flatten,get_groups,halve_group,get_max_dist
from alpha_shapes import alpha_shapes
from cech import cech
from persistence_diagrams import persistence_diagram,fix_infs
from clustering import cluster_distances
from dionysus import PersistenceDiagram
from draw import draw_bar_code_graph,draw_persistance_diagram
from sklearn.datasets import load_iris


classes = ['Setosa', 'Versicolour']#, 'Virginica']
data = load_iris()
# Take only two classes that are linearly separable.
X = data.data[:100]
y = data.target[:100]
Xs = flatten(map(halve_group, get_groups(X, y)))
Rs = map(get_max_dist, Xs)
# Chech uses to much memory on 100 examples.
cxs = map(alpha_shapes, Xs)
diagrams = [persistence_diagram(cx, R,n_intervals=None) for cx, R in zip(cxs, Rs)]
titles = flatten([[name + '_train', name + '_test'] for name in classes])
cluster_distances(map(lambda diagram: [PersistenceDiagram(d, diagram[d]) for d in range(3)], diagrams),
                  ps=[0,1,2], labels=titles, name="iris")
i = 0
for diagram in diagrams:
    diagram, max_j = fix_infs(diagram)
    draw_persistance_diagram(diagram, max_j, titles[i])
    draw_bar_code_graph(diagram, max_j, titles[i])
    i += 1
