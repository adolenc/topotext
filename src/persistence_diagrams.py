from dionysus import Simplex, Filtration, StaticPersistence, \
                     data_cmp, data_dim_cmp, DynamicPersistenceChains, \
                     init_diagrams
from math import floor

def fix_data(cx, max_r, n_intervals=10):
    """ Fix data for each sx in cx so that its birth falls onto integer
    interval [0, n_intervals), depending on its actual birth and max_r.
    """
    cx = sorted(cx, key=lambda sx: sx.data)
    for sx in cx:
        sx.data = floor(sx.data / max_r * (n_intervals-1))
    return cx

def to_dict(p):
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
    cx = fix_data(cx, max_r)
    f = Filtration(cx, data_dim_cmp)
    p = DynamicPersistenceChains(f)
    p.pair_simplices()
    dia = init_diagrams(p,f)
    print "diagram"
    print dia
    return dia

if __name__ == '__main__':
    from utils import read_cx
    cx = read_cx('cech.cx')
    max_r =  max(map(lambda sx:sx.data, cx))
    pd = persistence_diagram(cx, max_r)
    for d in range(3):
        print pd[d]
