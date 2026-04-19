import matplotlib.pyplot as plt
import numpy as np 
T = 100
n = 200

Z = np.random.choice([-1,1], size = (T,n))
Z[:,0] = 0
print(Z)
Z = np.cumsum(Z, axis = 1)
print(Z)

plt.title(label = "repartition des marches aléatoires")
plt.xlabel("temps T")
plt.ylabel("valeur de la marche")
plt.plot(Z.T) # transposee de Z 
plt.grid()
plt.show()

