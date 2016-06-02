from scipy.cluster import hierarchy
from scipy.spatial.distance import squareform
import numpy as np
from distances import bottleneck_distance
import dionysus
import matplotlib.pyplot as plt

def cluster_distances(diagrams, labels=None):
    x = ['one', 'two', 'three', 'four', 'five', 'six']
    d = np.zeros((len(diagrams), len(diagrams)))

    # Calculate distances on diagrams.
    for i,dia1 in enumerate(diagrams):
        for j,dia2 in enumerate(diagrams):
            d[i][j] = bottleneck_distance(dia1, dia2)

    y = squareform(d)
    Z = hierarchy.linkage(y)

    plt.figure(figsize=(25, 10))
    plt.title('Hierarchical Clustering Dendrogram')
    plt.xlabel('sample index')
    plt.ylabel('distance')
    hierarchy.dendrogram(
        Z,
        # orientation='left',
        # leaf_rotation=90.,  # rotates the x axis labels
        # leaf_font_size=8.,  # font size for the x axis labels
        labels=labels
    )
    plt.show()
    return Z


if __name__ == '__main__':
    d1 = dionysus.PersistenceDiagram(1)
    d1.append((1,4))
    d1.append((2,5))
    d1.append((1,6))
    d1.append((4,5))
    d1.append((3,7))

    d2 = dionysus.PersistenceDiagram(1)
    d2.append((1,3))
    d2.append((1,5))
    d2.append((2,6))
    d2.append((4,5))
    d2.append((6,7))

    d3 = dionysus.PersistenceDiagram(1)
    d3.append((2,3))
    d3.append((4,5))
    d3.append((2,6))
    d3.append((4,5))
    d3.append((6,7))

    d4 = dionysus.PersistenceDiagram(1)
    d4.append((1,3))
    d4.append((1,5))
    d4.append((2,6))

    d5 = dionysus.PersistenceDiagram(1)
    d5.append((2,6))
    d5.append((4,5))
    d5.append((6,7))

    cluster_distances([d1,d2,d3,d4,d5])

