import numpy as np
import scipy as sp
import scipy.io

from IPython import get_ipython
ip = get_ipython()
if not ip is None:
    ip.magic("%load_ext autoreload")
    ip.magic("%autoreload 2")

################################################################################
# Loading the data
################################################################################

import h5py
f = h5py.File('../data/MATS.mat', 'r')

y = f["y_sim"][:].reshape(-1, 1) * 1e10
y_img = f["y_km"][:].reshape(-1, 1)
m = y.shape[0]

xa = f["xa"][:].reshape(-1, 1) * 1e5
x_true = f["x_true"][:].reshape(-1, 1) * 1e10
n  = xa.shape[0]

data    = f["K"]["data"][:]
indices = f["K"]["ir"]
indptr  = f["K"]["jc"]
K = sp.sparse.csc_matrix((data, indices, indptr), shape = (m, n))

data    = f["Sainv"]["data"][:] * 1e-20
indices = f["Sainv"]["ir"]
indptr  = f["Sainv"]["jc"]
SaInv = sp.sparse.csc_matrix((data, indices, indptr), shape = (n, n))

data    = f["Seinv"]["data"][:] * 1e-20
indices = f["Seinv"]["ir"]
indptr  = f["Seinv"]["jc"]
SeInv = sp.sparse.csc_matrix((data, indices, indptr), shape = (m, m))

################################################################################
# Running invlib
################################################################################

from invlib.oem    import OEM
from invlib.vector import Vector
from invlib.mkl    import MklSparseCsc

K     = MklSparseCsc(K)
SaInv = MklSparseCsc(SaInv)
SeInv = MklSparseCsc(SeInv)
xa    = xa.view(Vector)
y     = y.view(Vector)

def aaa(x):
    xx = K.transpose_multiply(SeInv.multiply(K.multiply(x)))
    xx.add(SaInv.multiply(x))
    return xx

def compute_dx(x):
    dy = y - K.multiply(x.view(Vector))
    dx = K.transpose_multiply(dy.view(Vector))
    return dx

oem = OEM(K, SaInv, SeInv, xa, y)

dy = (K.multiply(xa) - y).view(Vector)
g  = K.transpose_multiply(SeInv.multiply(dy))
r  = (-g).view(Vector)
p  = (-r).view(Vector)
x0 = np.zeros(g.shape).view(Vector)

#x = oem.compute()
#103011 // -1.1308e+12
#0.000208998
#103011 // -1.1308e+12
#2.79346299509265e+17

