from os import listdir


def read_file(filename):
    """ Read a file into a string. """
    with open(filename, 'r') as f:
        return f.read().replace('\n', ' ')

def load_directory(directory):
    """ Return a list of strings containing text from all files in directory. """
    return [read_file(directory + '/' + f) for f in listdir(directory)]

def flatten(lst):
    """ Flatten shallow list LST. """
    return [e for l2 in lst for e in l2]
