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
