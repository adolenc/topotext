from dionysus import Simplex
from os import listdir
import numpy as np

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

def _write_matrix(X, input, separator=' '):
    """ Write matrix X to file, using separator between two entries. First line
    will contain number of rows and number of columns, separated by space.
    """
    rows, cols = len(X), len(X[0])
    input.write(str(rows) + ' ' + str(cols) + '\n')
    for row in X:
        input.write(separator.join(map(str, row)) + '\n')


def write_matrix(X, filename, separator=' '):
    """ Auxilary function that writes matrix to file.  """
    with open(filename, 'w') as f:
        _write_matrix(X, f, separator=separator)

def _read_cx(input):
    """ Read simplicial complex from input stream. Complex should be stored as
    a simplex per row along with the distance at which it is added into
    complex:
    distance <[comma separated list of vertices]>
    """
    def parse_line(line):
        r, sx = line.strip()[:-1].split('<')
        return Simplex(map(int, sx.split(',')), float(r))
    return [parse_line(line) for line in input]

def read_cx(filename):
    """ Auxilary function that reads complex from file.  """
    with open(filename, 'r') as f:
        return _read_cx(f)

def zipWith(x1, x2, fn):
    return [fn(p[0],p[1]) for p in zip(x1,x2)]

def get_groups(X, y):
    indices = [np.where(y==k) for k in np.unique(y)]
    return [X[i] for i in indices]
   
