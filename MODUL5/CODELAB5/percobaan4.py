# import matplotlib.pyplot as plt
# import numpy as np 

# x = [1,2,3,4,5]
# y = [3,7,2,8,5]

# plt.scatter(x,y) #ini tu titik doang gapake garis
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [3, 7, 2, 8, 5]

plt.plot(x, y, marker='o',  color='blue')

plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Simple Connected Scatter Plot')

plt.show()
