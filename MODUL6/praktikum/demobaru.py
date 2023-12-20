from PIL import Image, ImageOps, ImageEnhance, ImageFilter, ImageDraw, ImageFont

# Buka kedua gambar menggunakan Pillow
background = Image.open("D:/KULIAH UMM/Praktikum/SEM 5/FUNGSIONAL H/Praktikum_Fungsional2023/MODUL6/praktikum/images/bg.jpeg")
overlay = Image.open("D:/KULIAH UMM/Praktikum/SEM 5/FUNGSIONAL H/Praktikum_Fungsional2023/MODUL6/praktikum/images/logo.png")

# Ubah gambar background menjadi hitam-putih, berotasi 30 derajat, dan blur
background = background.convert("L")
background = ImageOps.grayscale(background)
rotated_background = background.rotate(30)
final_background = rotated_background.filter(ImageFilter.BLUR)

# Ubah tingkat kecerahan dan kontras gambar overlay
brightness_factor = 1.99  # Ganti dengan dua digit NIM terakhir x
contrast_factor = 1.99  # Ganti dengan dua digit NIM terakhir y
overlay_enhancer = ImageEnhance.Brightness(overlay.copy())
brightened_overlay = overlay_enhancer.enhance(brightness_factor)

contrast_enhancer = ImageEnhance.Contrast(brightened_overlay)
final_overlay = contrast_enhancer.enhance(contrast_factor)
final_overlay = final_overlay.resize((200, 200))  # Ganti dengan ukuran yang sesuai

# Periksa apakah gambar overlay memiliki alpha channel
if final_overlay.mode in ('RGBA', 'LA') or (final_overlay.mode == 'P' and 'transparency' in final_overlay.info):
    overlay_alpha = final_overlay.split()[3]
    position = (100, 100)  # Ganti dengan posisi yang sesuai
    final_background.paste(final_overlay, position, mask=overlay_alpha)
else:
    position = (100, 100)  # Ganti dengan posisi yang sesuai
    final_background.paste(final_overlay, position)

# Tambahkan teks pada gambar overlay
draw = ImageDraw.Draw(final_background)
font_path = "D:/KULIAH UMM/Praktikum/SEM 5/FUNGSIONAL H/Praktikum_Fungsional2023/MODUL6/codelab6part2/font/Arial MT Black from Ever Fonts.ttf"  # Ganti dengan path font Arial
font_size = 24
font = ImageFont.truetype(font_path, font_size)
text = "Informatika JOSSS!"
text_position = (50, 50)  # Ganti dengan posisi yang sesuai
draw.text(text_position, text, font=font, fill="white")

# Simpan gambar hasil edit
final_background.save("tugas_praktikum_enam.jpg")