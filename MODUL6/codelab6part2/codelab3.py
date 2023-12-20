from PIL import Image, ImageEnhance

# TODO 1 : Buka gambar dengan Pillow
image_path = "D:/KULIAH UMM/Praktikum/SEM 5/FUNGSIONAL H/Praktikum_Fungsional2023/MODUL6/codelab6part2/images/switzerland.jpg"
image = Image.open(image_path)

# TODO 2 : Ubah tingkat kecerahan dan kontras
brightness_factor = 1.5
contrast_factor = 1.2

# Ubah tingkat kecerahan
brightness_enhancer = ImageEnhance.Brightness(image)
brightened_image = brightness_enhancer.enhance(brightness_factor)

# Ubah tingkat kontras
contrast_enhancer = ImageEnhance.Contrast(brightened_image)
final_image = contrast_enhancer.enhance(contrast_factor)

# TODO 3 : Simpan gambar hasil edit
final_image.save("brightness_contrast_image.jpg")

# TODO 4 : Tampilkan
final_image.show()
