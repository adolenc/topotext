from dionysus import Simplex, Filtration, StaticPersistence, \
                     data_cmp, data_dim_cmp, DynamicPersistenceChains, \
                     init_diagrams, PersistenceDiagram
from math import floor
import numpy as np

def replace(l, v1, v2):
    """ In a list of doubles l, replace every occurance of v1
    with v2 in the second element of the double. """
    return [(x[0], v2) if x[1] == v1 else x for x in l]

def fix_infs(pers):
    """ Replace positive infs in persistances (dictionary that has a list of doubles as values). """
    max_j = int(np.unique(sorted([l[1] for key in pers for l in pers[key]]))[-2])
    pers = {key : replace(pers[key], float("inf"), max_j) for key in pers}
    return pers, max_j

def fix_data(cx, max_r, n_intervals=10):
    """ Fix data for each sx in cx so that its birth falls onto integer
    interval [0, n_intervals), depending on its actual birth and max_r.
    """
    for sx in cx:
        if sx.data > max_r:
            print "WOWOWOW", sx, max_r
        sx.data = floor(sx.data / max_r * (n_intervals-1))
    return cx

def to_dict(p, f, max_dim):
    smap = p.make_simplex_map(f)
    diagrams = {}
    for i in (i for i in p if i.sign()):
        b = smap[i]
        if b.dimension() > max_dim: break
        if b.dimension() not in diagrams:
            diagrams[b.dimension()] = []
        if i.unpaired():
            diagrams[b.dimension()].append((b.data, float('inf')))
        else:
            d = smap[i.pair()]
            diagrams[b.dimension()].append((b.data, d.data))
    return diagrams

def persistence_diagram(cx, max_r, max_dim=2):
    """ Compute persistence diagrams for cx, given max_r as the maximum
    distance between two points upto max_dim dimensions.
    """
    cx.sort(data_dim_cmp)
    cx = fix_data(cx, max_r)
    f = Filtration(cx, data_dim_cmp)
    p = StaticPersistence(f)
    p.pair_simplices()
    return to_dict(p, f, max_dim)

if __name__ == '__main__':
    from utils import read_cx
    cx = read_cx('cech.cx')
    max_r =  max(map(lambda sx:sx.data, cx))
    pd = persistence_diagram(cx, max_r)
    for d in range(3):
        print pd[d]
