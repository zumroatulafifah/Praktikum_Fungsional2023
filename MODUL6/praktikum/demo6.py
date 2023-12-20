from PIL import Image, ImageEnhance, ImageDraw, ImageFont, ImageFilter

# Buka kedua gambar menggunakan Pillow
background_image_path = "D:/KULIAH UMM/Praktikum/SEM 5/FUNGSIONAL H/Praktikum_Fungsional2023/MODUL6/praktikum/images/UMM.jpg"
overlay_image_path = "D:/KULIAH UMM/Praktikum/SEM 5/FUNGSIONAL H/Praktikum_Fungsional2023/MODUL6/praktikum/images/lambang umm.png"

background_image = Image.open(background_image_path)
overlay_image = Image.open(overlay_image_path)

# Ubah tingkat kecerahan dan kontras gambar overlay
brightness_factor = 1.9
contrast_factor = 1.9

# Ubah tingkat kecerahan dan kontras
overlay_enhancer = ImageEnhance.Brightness(overlay_image)
brightened_overlay = overlay_enhancer.enhance(brightness_factor)
overlay_enhancer = ImageEnhance.Contrast(brightened_overlay)
final_overlay = overlay_enhancer.enhance(contrast_factor)

# Jika ada saluran alpha (RGBA), buat mask alpha
if 'A' in final_overlay.getbands():
    overlay_alpha = final_overlay.split()[3]
    mask_alpha = Image.new("L", final_overlay.size, 255)
    mask_alpha.paste(overlay_alpha, (0, 0))

    # Sisipkan gambar overlay ke dalam gambar background
    x_center = (background_image.width - final_overlay.width) // 2
    y_center = (background_image.height - final_overlay.height) // 2

    # Paste gambar overlay dengan mask alpha
    background_image.paste(final_overlay, (x_center, y_center), mask=mask_alpha)

    # Tambahkan teks pada gambar overlay
    draw = ImageDraw.Draw(background_image)
    font_path = "D:/KULIAH UMM/Praktikum/SEM 5/FUNGSIONAL H/Praktikum_Fungsional2023/MODUL6/codelab6part2/font/Arial MT Black from Ever Fonts.ttf"
    font_size = 24
    font = ImageFont.truetype(font_path, font_size)
    text = "Informatika JOSSS!"

    # Hitung lebar dan tinggi teks
    text_width, text_height = draw.textsize(text, font=font)

    # Tentukan posisi teks di tengah gambar overlay
    text_x = (background_image.width - text_width) // 2
    text_y = (background_image.height - text_height) // 2

    draw.text((text_x, text_y), text, font=font, fill="white")

    # Simpan gambar hasil edit
    background_image.save("tugas_praktikum_enam.jpg")

    # Tampilkan hasil edit
    background_image.show()
else:
    print("Gambar overlay tidak memiliki saluran alpha (transparansi)")
