from dionysus import Simplex
from os import listdir

def read_file(filename):
    """ Read a file into a string. """
    with open(filename, 'r') as f:
        return f.read().decode('utf-8').replace('\n', ' ')

def load_directory(directory):
    """ Return a list of strings containing text from all files in directory. """
    return [read_file(directory + '/' + f) for f in listdir(directory)]

def flatten(lst):
    """ Flatten shallow list LST. """
    return [e for l2 in lst for e in l2]

def write_matrix(X, filename, separator=' '):
    """ Write matrix X to file, using separator between two entries. First line
    will contain number of rows and number of columns, separated by space.
    """
    with open(filename, 'w') as f:
        rows, cols = len(X), len(X[0])
        f.write(str(rows) + ' ' + str(cols) + '\n')
        for row in X:
            f.write(separator.join(map(str, row)) + '\n')

def read_cx(filename):
    """ Read simplicial complex from file. Complex should be stored as a
    simplex per row along with the distance at which it is added into
    complex:
    distance <[comma separated list of vertices]>
    """
    def parse_line(line):
        r, sx = line.strip()[:-1].split('<')
        return Simplex(map(int, sx.split(',')), float(r))
    with open(filename, 'r') as f:
        return [parse_line(line) for line in f]

def zip_with(x1, x2, fn):
    return [fn(p[0],p[1]) for p in zip(x1,x2)]

def avg(array):
    return sum(array)/len(array)

def map_flatten(array):
    return map(flatten, array)

def map_map(fn, array):
    return map(lambda x: map(fn, x), array)