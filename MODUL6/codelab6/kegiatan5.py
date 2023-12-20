#rotate the image by an angle

import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('D:/KULIAH UMM/Praktikum/SEM 5/FUNGSIONAL H/Praktikum_Fungsional2023/MODUL6/codelab6/images/afifah.jpg')
rotated_image = img.rotate(90)
plt.imshow(rotated_image)
plt.axis('off') 
plt.show()