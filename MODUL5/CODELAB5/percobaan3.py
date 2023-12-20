import matplotlib.pyplot as plt
import numpy as np 

y1 = np.array([3,8,1,10])
y2 = np.array([6,2,7,11])

plt.plot(y1, label = 'Garis 1')
plt.plot(y2, label = 'Garis 2')

plt.title('Plot Dua Garis')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

plt.legend()
plt.show()

#karena gaada x jadi dihubungkan dengan index array