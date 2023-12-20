#change size image

import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('D:/KULIAH UMM/Praktikum/SEM 5/FUNGSIONAL H/Praktikum_Fungsional2023/MODUL6/codelab6/images/afifah.jpg')
new_size = (800, 600)
resized_image = img.resize(new_size)
plt.imshow(resized_image)
plt.axis('off') 
plt.show()