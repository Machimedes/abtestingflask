import numpy as np

p = np.matrix([
    [0.1, 0.8, 0.3],
    [0.5, 0.1, 0.6],
    [0.4, 0.1, 0.1]])

v, q = np.linalg.eig(p)
q_ = np.linalg.inv(q)

print(q[:, 0])

norms = np.linalg.norm(p, axis=1)

pn = [[0.9], [0.05], [0.05]]
for num in range(0, 10):
    pn = p @ pn
s = np.ndarray.min(pn, axis=0)
c = pn / s
print(c)

pn = [[0.4], [0.3], [0.3]]
for num in range(0, 10):
    pn = p @ pn
s = np.ndarray.min(pn, axis=0)
c = pn / s
print(c)

pn = [[0.5], [100], [0.8]]
for num in range(0, 10):
    pn = p @ pn
s = np.ndarray.min(pn, axis=0)
c = pn / s
print(c)
