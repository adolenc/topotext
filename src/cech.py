from dionysus import *
from utils import read_cx
import shutil
import os
import subprocess

def make_tmp_dir(tmpdir='tmp'):
    """ Create temporary directory. """
    if not os.path.exists(tmpdir):
        os.makedirs(tmpdir)
    return tmpdir

def rm_tmp_dir(tmpdir='tmp'):
    """ Remove temporary directory. """
    shutil.rmtree(tmpdir)

def cech(X, tmpdir='tmp', cech_cx_binary='./cpp/cech_cx'):
    """ Wrapper around cpp/cech_cx.cc in python. Creates a tmpdir directory
    which it uses for storing communication between two processes.
    """
    tmp_X_file =  tmpdir + '/X.mat'
    tmp_cech_cx_file = tmpdir + '/cech.cx'
    make_tmp_dir(tmpdir)
    write_matrix(X, tmp_X_file)
    with open(tmp_X_file, 'r') as fi:
        with open(tmp_cech_cx_file, 'w') as fo:
            fo.write(subprocess.check_output([cech_cx_binary], stdin=fi))
    rm_tmp_dir(tmpdir)
    return read_cx(tmp_cech_cx_file)

if __name__ == "__main__":
    from preprocessor import *
    from prepreprocessor import *
    pp = Preprocessor(Prepreprocessor, [], use_tfidf=3)
    X, _ = pp.process(['../data/abstracts/', '../data/sports'])
    for sx in cech(X, tmpdir='cech_tmp'):
        print sx
