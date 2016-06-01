from dionysus import *
from utils import read_cx
import shutil
import os
import subprocess

def make_tmp_dir(tmpdir):
    """ Create temporary directory. """
    if not os.path.exists(tmpdir):
        os.makedirs(tmpdir)
    return tmpdir

def rm_tmp_dir(tmpdir):
    """ Remove temporary directory. """
    shutil.rmtree(tmpdir)

def cech(X, tmpdir='tmp', cech_cx_binary='./cpp/cech_cx'):
    """ Wrapper around cpp/cech_cx.cc in python. Creates a tmpdir directory
    which it uses for storing communication between two processes.
    """
    make_tmp_dir(tmpdir)
    tmp_X_file =  tmpdir + '/X.mat'
    tmp_cech_cx_file = tmpdir + '/cech.cx'
    write_matrix(X, tmp_X_file)
    with open(tmp_X_file, 'r') as fi:
        with open(tmp_cech_cx_file, 'w') as fo:
            fo.write(subprocess.check_output([cech_cx_binary], stdin=fi))
    cx = read_cx(tmp_cech_cx_file)
    rm_tmp_dir(tmpdir)
    return cx

if __name__ == "__main__":
    for sx in cech([[1,2,3], [3,4,5], [6,7,8], [9,1,2]], tmpdir='cech_tmp'):
        print sx
