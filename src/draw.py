import matplotlib.pyplot as plt
import numpy as np

def replace(l, v1, v2):
    return [(x[0], v2) if x[1] == v1 else x for x in l]

def fix_infs(persistances):
    max_j = int(np.unique(sorted([l[1] for key in persistances for l in persistances[key]]))[-2])
    for key in persistances:
        persistances[key] = replace(persistances[key], float("inf"), max_j)
    return persistances
        
def draw_persistance_diagram(persistances):
    for key in persistances:
        #TODO: add a y=x line in each graph
        plt.figure()
        plt.scatter([x[0] for x in persistances[key]], [x[1] for x in persistances[key]])
        plt.show()

if __name__ == "__main__":
    #input: dictionary - keys are dimensions of homology groups (1,2 and 3),
    #values are lists of tuples (coordinates (i,j)) representing persistances of simplices
    persistances = {1: [(1,2), (4,5), (2, float("inf")), (1,4), (4,5)],
                    2: [(2,5), (1,3)],
                    3: [(3,4), (3, float("inf"))]}
    print fix_infs(persistances)
    draw_persistance_diagram(persistances)
