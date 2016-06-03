import matplotlib.pyplot as plt
import numpy as np
from persistence_diagrams import fix_infs,replace

def draw_persistance_diagram(pers, max_j, title):
    i = 1
    plt.figure(figsize=(25, 10))
    for key in pers:
        plt.subplot(130 + i, aspect='equal')
        plt.axis([0, max_j+1, 0, max_j+1])
        plt.title('$H_{' + str(i-1) + '}$', fontsize=18)
        plt.xlabel("i")
        plt.ylabel("j")
        plt.plot([0, max_j+1], [0, max_j + 1], color="gray")
        plt.scatter([x[0] for x in pers[key]], [x[1] for x in pers[key]], s=15)
        i += 1
    plt.suptitle('Persistance diagrams for first three homologies: ' + title, fontsize=16)
    plt.tight_layout(h_pad=0.2)
    # plt.show()
    plt.savefig('../figures/pers_diagram_'+title+'.png', bbox_inches='tight')

def sort_list_of_tuples(l):
    return list(reversed(sorted(l, key=lambda x: (x[0], -x[1]))))

def draw_bar_code_graph(pers, max_j, title):
    i = 1
    plt.figure(figsize=(25, 10))
    for key in pers:
        h = sort_list_of_tuples(pers[key])
        no_cx = len(h) #number of simplexes in this dimension
        plt.subplot(310 + i).get_yaxis().set_visible(False)
        plt.axis([0, max_j+1, 0, no_cx+1])
        # plt.xticks(range(max_j+1))
        plt.ylabel('$H_{' + str(i-1) + '}$', fontsize=18)
        plt.xlabel("[birth, death]")
        for k in range(no_cx):
            i_, j_ = h[k]
            plt.plot([i_, j_ + 1e-1], [k+1, k+1], color="green", lw=4)
        i += 1
    plt.suptitle('Bar code graph for first three homologies: ' + title, fontsize=16)
    plt.tight_layout(pad=3.5, h_pad=0.4)
    # plt.show()
    plt.savefig('../figures/bar_code_diagram_' + title + '.png', bbox_inches='tight')

if __name__ == "__main__":
    #input: dictionary - keys are dimensions of homology groups (1,2 and 3),
    #values are lists of tuples (coordinates (i,j)) representing pers of simplices
##    pers = {1: [(1,2), (4,5), (2, float("inf")), (1,4), (4,5)],
##            2: [(2,5), (1,3)],
##            3: [(3,4), (3, float("inf"))]}
    pers = {1: [(x, y) for x in np.random.random_integers(1,10,10) for y in np.random.random_integers(x,30,10)],
            2: [(1, y) for y in np.random.random_integers(1,30,100)],
            3: [(3,3), (3,3), (3,3), (3,3), (3, float("inf"))]}
    pers, max_j = fix_infs(pers)
##    print pers
    draw_persistance_diagram(pers, max_j)
    draw_bar_code_graph(pers, max_j)
