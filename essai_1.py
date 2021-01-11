import numpy as np
import matplotlib.pyplot as plt

grid = np.linspace(-1/2,1/2,10000)

for N in [5,10,20,40,80,160] :
	coef = 2*np.sin(np.pi*np.arange(1,N)/2)/(np.pi*np.arange(1,N))
	plt.plot(grid,0.5+(coef[None,:]*np.cos(2*np.pi*np.arange(1,N) [None, : ]*grid[:, None])).sum(1),label='N = {}'.format(N))
	plt.legend()
	plt.show()
	#change