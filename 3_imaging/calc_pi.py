#program to calculate digits of pi

import numpy as np
import matplotlib.pyplot as plt

#Compare to Gregory formula
n_iter = 100
pi_gregory = []
sum = 0.0
for i in range(0,n_iter):
  sum = sum+(-1)**i/(2*i+1.0)
  pi_gregory.append(sum*4.0)

plt.figure()
plt.plot(range(0,n_iter),pi_gregory)

error_gregory = [x-np.pi for x in pi_gregory]
plt.figure()
plt.semilogy(error_gregory,'g.')
plt.show()
