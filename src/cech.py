from dionysus import *
from utils import _read_cx,_write_matrix
import StringIO
import subprocess

def cech(X, cech_cx_binary='./cpp/cech_cx'):
    """ Wrapper around cpp/cech_cx.cc in python. Creates a tmpdir directory
    which it uses for storing communication between two processes.
    """
    X_str = StringIO.StringIO()
    _write_matrix(X, X_str)
    pr = subprocess.Popen([cech_cx_binary], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    cech_cx_out = pr.communicate(input=X_str.getvalue())[0].decode()
    return _read_cx(StringIO.StringIO(cech_cx_out))

if __name__ == "__main__":
    X = [[1,2,3], [3,4,5], [6,7,8], [9,1,2]]
    for sx in cech(X):
        print sx
