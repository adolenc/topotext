from utils import flatten,get_groups,halve_group,get_max_dist
from alpha_shapes import alpha_shapes
from cech import cech
from persistence_diagrams import persistence_diagram,fix_infs
from clustering import cluster_distances
from dionysus import PersistenceDiagram
from draw import draw_bar_code_graph,draw_persistance_diagram
from sklearn.datasets import make_circles
from random import random
import numpy as np


def generate_circles(n, y_val):
    """
    Generates a dataset where points are shaped into two circles,
    and labels them with y_val.
    """
    X,y = make_circles(n, noise=0.1)

    return (X, [y_val] * len(X))


def generate_line(n, y_val):
    """
    Generates dataset where points are shaped in a line,
    and labels then with y_val.
    """
    noise=0.1
    X = map(lambda p: [p+(random()*noise),p+(random()*noise)], [random() for _ in range(n)])
    return (X, [y_val] * len(X))


if __name__ == '__main__':
    X1,y1 = generate_circles(20, 0)
    X2,y2 = generate_line(20, 1)

    X = np.vstack((X1,X2))
    y = y1 + y2

    classes = ['circles', 'lines']
    Xs = flatten(map(halve_group, get_groups(X, y)))
    Rs = map(get_max_dist, Xs)
    cxs = map(cech, Xs)
    diagrams = [persistence_diagram(cx, R) for cx, R in zip(cxs, Rs)]
    titles = flatten([[name + '_train', name + '_test'] for name in classes])
    cluster_distances(map(lambda diagram: [PersistenceDiagram(d, diagram[d]) for d in range(3)], diagrams), ps=[0,1,2],
                      labels=titles, name="toy")
    i = 0
    for diagram in diagrams:
        diagram, max_j = fix_infs(diagram)
        draw_persistance_diagram(diagram, max_j, titles[i])
        draw_bar_code_graph(diagram, max_j, titles[i])
        i += 1
