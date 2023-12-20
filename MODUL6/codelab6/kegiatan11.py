import matplotlib.pyplot as plt
from PIL import Image, ImageFilter

img = Image.open('D:/KULIAH UMM/Praktikum/SEM 5/FUNGSIONAL H/Praktikum_Fungsional2023/MODUL6/codelab6/images/afifah.jpg')

if img.mode != "RGB":
    img = img.convert("RGB")

resized_image = img.resize((300, 200))

blurred_image = resized_image.filter(ImageFilter.GaussianBlur(radius=2))

plt.imshow(blurred_image)
plt.title("\nGambar yang Diblur")
plt.axis("off")
plt.show()
