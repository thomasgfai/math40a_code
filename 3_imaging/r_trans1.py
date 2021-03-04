import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import radon,iradon,rescale

# Black image with white square
I=np.zeros((100,100))
I[25:75,25:75]=1

# Radon transform at angle 0 and 45
theta=np.linspace(0.,180.,max(I.shape),endpoint=True)
R = radon(I, theta=theta)

# Plot the image
plt.figure()
plt.subplot(2,1,1)
plt.imshow(I,cmap=plt.cm.Greys_r,interpolation='nearest')
plt.subplot(2,1,2)
plt.plot(R[:,0],'-',linewidth=2)
plt.axis('scaled')
plt.axis([0,np.shape(R)[0],-1,np.shape(R)[0]])
plt.show()
