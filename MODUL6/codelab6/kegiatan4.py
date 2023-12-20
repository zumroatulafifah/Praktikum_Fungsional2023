#cut image based on cordinat 

import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('D:/KULIAH UMM/Praktikum/SEM 5/FUNGSIONAL H/Praktikum_Fungsional2023/MODUL6/codelab6/images/afifah.jpg')
box = (100,100,400,300)
cropped_image = img.crop(box)
plt.imshow(cropped_image)
plt.axis('off') 
plt.show()