from dionysus import Rips, PairwiseDistances, Filtration

def vietoris_rips(X, skeleton=5, max=10000):
    """ Generate the Vietoris-Rips complex on the given set of points in 2D.
    Only simplexes up to dimension skeleton are computed.
    The max parameter denotes the distance cut-off value.
    """
    distances = PairwiseDistances(X.tolist())
    rips = Rips(distances)
    simplices = Filtration()
    rips.generate(skeleton, max, simplices.append)
    for sx in simplices:
        sx.data = rips.eval(sx)
    return simplices
