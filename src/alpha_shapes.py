from dionysus import *
import numpy as np
from sklearn.decomposition import PCA
from math import sqrt

def reduce_n_columns(X, n=3):
    """ Use PCA to reduce number of columns in X to n. """
    if len(X[0]) <= n: return X
    pca = PCA(n)
    return pca.fit_transform(X)

def alpha_shapes(X):
    X = reduce_n_columns(X)
    cx = Filtration()
    fill_alpha_complex(X.tolist(), cx)
    for sx in cx: # we need data to be just distances at which sx was added to cx
        sx.data = sqrt(sx.data[0])
    return cx

if __name__ == '__main__':
    X = np.array([[0, 0, 0],
                  [1, 0, 0.0000000001],
                  [1, 1, 0],
                  [5, 1, 0]])
    alpha_shapes_cx = alpha_shapes(X)
    for s in sorted(alpha_shapes_cx, key=lambda sx:sx.data):
        print s
