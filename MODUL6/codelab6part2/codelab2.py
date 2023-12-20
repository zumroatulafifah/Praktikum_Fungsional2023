from PIL import Image

# TODO 0 : Import beberapa library lain yang dibutuhkan
# (Library sudah di-import pada baris pertama)

# TODO 1 : Buka gambar latar belakang (background) dan gambar yang ingin disisipkan (overlay)
background_image_path = "D:/KULIAH UMM/Praktikum/SEM 5/FUNGSIONAL H/Praktikum_Fungsional2023/MODUL6/codelab6part2/images/switzerland.jpg"
overlay_image_path = "D:/KULIAH UMM/Praktikum/SEM 5/FUNGSIONAL H/Praktikum_Fungsional2023/MODUL6/codelab6part2/images/afifah.jpg"
background_image = Image.open(background_image_path)
overlay_image = Image.open(overlay_image_path)

# TODO 2 : Konversi overlay image ke mode RGBA (menghilangkan alpha channel)
if overlay_image.mode != "RGBA":
    overlay_image = overlay_image.convert("RGBA")

# TODO 3 : (optional) Perkecil ukuran gambar overlay menggunakan method resize()
# Ubah nilai width dan height sesuai kebutuhan
new_size = (100, 100)
overlay_image = overlay_image.resize(new_size)

# Verifikasi dan konversi eksplicit ke mode RGB
if overlay_image.mode != "RGB":
    overlay_image = overlay_image.convert("RGB")

# Tentukan/Hitung koordinat tengah untuk menempatkan overlay
x_center = (background_image.width - overlay_image.width) // 2
y_center = (background_image.height - overlay_image.height) // 2

# TODO 4 : Buat mask dari alpha channel overlay_image
if len(overlay_image.split()) == 4:
    _, _, _, overlay_mask = overlay_image.split()
else:
    overlay_mask = None  # If there is no alpha channel

# TODO 5 : Sisipkan gambar overlay ke dalam gambar background menggunakan method paste()
background_image.paste(overlay_image, (x_center, y_center), overlay_mask)

# TODO 6 : Simpan gambar hasil edit
background_image.save("hasil_edit_gambar.jpg")

# TODO 7 : Tampilkan
background_image.show()
