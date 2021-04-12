dtype = 'float32'

import os
os.environ['THEANO_FLAGS'] = f'floatX={dtype},device=cuda'

import pymc3 as pm
import numpy as np

N, P   = 100000, 100
n_iter = 100000


X    = np.random.randn(N, P).astype(dtype)
beta = np.random.randn(P, 1).astype(dtype)
eps  = np.random.randn(N, 1).astype(dtype)

y = X @ beta + eps

with pm.Model():
    coef = pm.Normal('coef', shape=(P,1))
    likelihood = pm.Normal('likelihood', mu=pm.math.dot(X, coef), observed=y)
    approx = pm.fit(n_iter)