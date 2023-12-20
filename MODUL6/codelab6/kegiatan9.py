import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('D:/KULIAH UMM/Praktikum/SEM 5/FUNGSIONAL H/Praktikum_Fungsional2023/MODUL6/codelab6/images/afifah.jpg')

sepia_matrix = [
    0.393, 0.769, 0.189, 0,
    0.349, 0.686, 0.168, 0,
    0.272, 0.534, 0.131, 0,
]

sepia_image = img.convert('RGB', matrix=sepia_matrix)
plt.imshow(sepia_image)
plt.axis('off')
plt.show()
