from dionysus import *
import numpy as np
from sklearn.decomposition import PCA

def pca_proj(feature_matrix, n_comp=3):
    pca = PCA(n_comp)
    return pca.fit_transform(feature_matrix)

def alpha_shapes(feature_matrix):
    cx = Filtration()
    fill_alpha_complex(feature_matrix.tolist(), cx)
##    alphashape = [s for s in cx if s.data[0] <= .5]
    for s in cx: print s

if __name__ == '__main__':
    feature_matrix = np.reshape(np.random.sample(70), (10,7))
    projection = pca_proj(feature_matrix, 2)
    print projection
    alpha_shapes(projection)
