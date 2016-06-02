from dionysus import *
import numpy as np
from sklearn.decomposition import PCA

def pca_proj(feature_matrix, n_comp=3):
    pca = PCA(n_comp)
    return pca.fit_transform(feature_matrix)

def alpha_shapes(feature_matrix):
    cx = Filtration()
    projection = pca_proj(feature_matrix) #pca
    fill_alpha_complex(projection.tolist(), cx)
    for sx in cx:
        sx.data = sx.data[0]
    return cx

if __name__ == '__main__':
    feature_matrix = np.reshape(np.random.sample(70), (10,7)) #sample matrix
    projection = pca_proj(feature_matrix) #pca
    alpha_shapes_cx = alpha_shapes(projection) #calculate alpha shapes
    #iterate over the simplices in the complex (Filtration class)
    for s in alpha_shapes_cx:
        print s, s.data[0]
