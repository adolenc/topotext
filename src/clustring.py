from sklearn.cluster import hierarchical
from sklearn.datasets import load_iris

if __name__ == '__main__':
    clstr = hierarchical.AgglomerativeClustering(n_clusters=3)
    data = load_iris()
    print clstr.fit_predict(data.data)