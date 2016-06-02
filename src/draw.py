import matplotlib.pyplot as plt
import numpy as np

def replace(l, v1, v2):
    return [(x[0], v2) if x[1] == v1 else x for x in l]

def fix_infs(pers):
    global max_j
    max_j = int(np.unique(sorted([l[1] for key in pers for l in pers[key]]))[-2])
    pers = {key : replace(pers[key], float("inf"), max_j) for key in pers}
    return pers
        
def draw_persistance_diagram(pers):
    i = 1
    plt.figure()
    for key in pers:
        plt.subplot(310 + i)
        plt.axis([0, max_j+1, 0, max_j+1])
        plt.ylabel('$H_{' + str(i-1) + '}$', fontsize=18)
        plt.plot([0, max_j+1], [0, max_j + 1], color="gray")
        plt.scatter([x[0] for x in pers[key]], [x[1] for x in pers[key]])
        i += 1
    plt.suptitle('Persistance diagrams for first three homologies', fontsize=16)
    plt.tight_layout(pad=2, h_pad=0.2)
    plt.show()

def draw_bar_code_graph(pers):
    pass

if __name__ == "__main__":
    #input: dictionary - keys are dimensions of homology groups (1,2 and 3),
    #values are lists of tuples (coordinates (i,j)) representing pers of simplices
    pers = {1: [(1,2), (4,5), (2, float("inf")), (1,4), (4,5)],
                    2: [(2,5), (1,3)],
                    3: [(3,4), (3, float("inf"))]}
    pers = fix_infs(pers)
    print pers
    draw_persistance_diagram(pers)
