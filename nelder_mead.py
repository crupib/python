import numpy as np
from scipy.optimize import minimize, rosen

x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
res = minimize(rosen, x0, method='nelder-mead')
		
print(res.x)
