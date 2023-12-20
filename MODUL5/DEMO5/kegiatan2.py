import matplotlib.pyplot as plt
import numpy as np

data_transaksi = [
    ("Produk A", 50, 10),
    ("Produk B", 30, 25),
    ("Produk C", 20, 30),
    ("Produk D", 60, 8),
    ("Produk E", 40, 15),
    ("Produk F", 70, 5),
]

# TODO 1: Ekstrak harga produk dan jumlah produk terjual untuk visualisasi pertama
harga_produk, jumlah_terjual = zip(*[(harga, jumlah) for _, harga, jumlah in data_transaksi])

# TODO 2: Buat scatter plot untuk hubungan antara harga produk dan jumlah produk terjual
plt.figure(figsize=(8, 6))
plt.scatter(harga_produk, jumlah_terjual, color='purple', marker='o')
plt.xlabel('Harga Produk')
plt.ylabel('Jumlah Produk Terjual')
plt.title('Hubungan Harga Produk dan Jumlah Produk Terjual')

# TODO 3: Hitung total pendapatan untuk setiap produk
pendapatan_produk = [harga * jumlah for _, harga, jumlah in data_transaksi]

# TODO 4: Tambahkan bar chart untuk menyajikan pendapatan produk
fig, ax = plt.subplots(figsize=(8, 6))
produk_labels = [produk for produk, _, _ in data_transaksi]
bar_chart = ax.bar(produk_labels, pendapatan_produk, color='purple')
ax.set_ylabel('Pendapatan')
ax.set_title('Pendapatan Produk')

# Menambahkan label untuk setiap bar
for idx, rect in enumerate(bar_chart):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height, f'{height}', ha='center', va='bottom')

plt.show()
