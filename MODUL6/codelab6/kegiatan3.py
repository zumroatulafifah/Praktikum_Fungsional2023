#make copy image with max size

import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('D:/KULIAH UMM/Praktikum/SEM 5/FUNGSIONAL H/Praktikum_Fungsional2023/MODUL6/codelab6/images/afifah.jpg')
max_size = (400, 400)
img.thumbnail(max_size)
plt.imshow(img)
plt.axis('off') 
plt.show()