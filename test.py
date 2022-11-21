import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 10.0, 3)
y1 = 2. - 0.5*x
y2 = -1 + 1.5*x
theta = np.linspace(-90.0, 90.0 ,1801)

# for i in range(len(x)):
#     theta = np.arcsin(y[i]/x[i])
#     rho = np.sqrt(y[i]**2 + x[i]**2)
#     plt.plot(theta, rho)

for j in range(len(x)):
    rho1 = x[j]*np.sin(theta) + y1[j]*np.sin(theta)
    rho2 = x[j]*np.sin(theta) + y2[j]*np.sin(theta)
    plt.plot(theta, rho1)
    plt.plot(theta, rho2)

plt.xlim(0,7)
plt.show()
