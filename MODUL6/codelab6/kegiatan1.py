#open image from path

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('D:/KULIAH UMM/Praktikum/SEM 5/FUNGSIONAL H/Praktikum_Fungsional2023/MODUL6/codelab6/images/afifah.jpg')
plt.imshow(img)
plt.axis('off') 
plt.show()