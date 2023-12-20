from PIL import Image, ImageDraw, ImageFont

# TODO 0: Import library lain yang dibutuhkan

# TODO 1: Lakukan load image pada variabel berikut
# hint: kalian bisa gunakan fungsi open()
gambarku = Image.open('D:/KULIAH UMM/Praktikum/SEM 5/FUNGSIONAL H/Praktikum_Fungsional2023/MODUL6/codelab6part2/images/afifah.jpg')

# TODO 2: Ubah gambar menjadi hitam-putih
# hint: kalian bisa gunakan fungsi convert()
gambarBW = gambarku.convert("L")

# TODO 3: Tambahkan text sesuai kriteria.
draw = ImageDraw.Draw(gambarBW)

# Tentukan teks (ganti dengan nama dan NIM kalian)
text = "Nama: Zumro'atul Afifah, NIM : 202110370311099"

# Tentukan font dan ukuran font
direktoriFont = "D:/KULIAH UMM/Praktikum/SEM 5/FUNGSIONAL H/Praktikum_Fungsional2023/MODUL6/codelab6part2/font/Arial MT Black from Ever Fonts.ttf"
size = 24
font = ImageFont.truetype(direktoriFont, size)

# Hitung lebar dan tinggi teks
text_bbox = draw.textbbox((0, 0), text, font=font)
#textbox ini buat kotak pembatas
text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
#menghitung lebar dan tinggi teks dengan mengambil selisih antara kordinat x dan y dari kotak pembatas

# Tentukan posisi teks di tengah gambar
text_x = (gambarBW.width - text_width) // 2
text_y = (gambarBW.height - text_height) // 2

# Tambahkan teks ke gambar
draw.text((text_x, text_y), text, font=font, fill=255)

# TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
gambarBW.save("percobaan_satu.jpg")

# TODO 5: Tampilkan hasil akhir gambar
gambarBW.show()
