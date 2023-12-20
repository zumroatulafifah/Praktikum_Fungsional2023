#make blur image

import matplotlib.pyplot as plt
from PIL import Image, ImageFilter

img = Image.open('D:/KULIAH UMM/Praktikum/SEM 5/FUNGSIONAL H/Praktikum_Fungsional2023/MODUL6/codelab6/images/afifah.jpg')
blurred_image = img.filter(ImageFilter.GaussianBlur(radius=2))
plt.imshow(blurred_image)
plt.axis('off') 
plt.show()