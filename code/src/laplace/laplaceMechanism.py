import numpy as np

print('Laplace mechanism')
mean, scale = 0., 1.
s = np.random.laplace(mean, scale, 1)[0]
print(s)
