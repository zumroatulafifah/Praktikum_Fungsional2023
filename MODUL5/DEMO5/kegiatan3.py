import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm #distribusi normal 

# Data tinggi badan
tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160]
interval_size = 10

# Fungsi untuk mengelompokkan tinggi badan ke dalam interval tertentu
def kelompokkan_ke_interval(data, interval_size, start_interval):
    return [((x - start_interval) // interval_size) * interval_size + start_interval for x in data]

# Menghitung frekuensi tinggi badan dalam interval, merangkum data biar terorganisir dalam interval
def hitung_frekuensi(data, interval_size, start_interval):
    intervals = kelompokkan_ke_interval(data, interval_size, start_interval)
    frekuensi = {interval: intervals.count(interval) for interval in set(intervals)}
    return frekuensi

# Visualisasi histogram dan kurva PDF
def visualisasi_histogram_dan_pdf(data, interval_size, start_interval):
    frekuensi = hitung_frekuensi(data, interval_size, start_interval)
    intervals = sorted(frekuensi.keys())
    counts = [frekuensi[interval] for interval in intervals]

    plt.bar(intervals, counts, width=interval_size, edgecolor='black', alpha=0.7, label='Histogram')

    # Kurva PDF distribusi normal
    mu, sigma = np.mean(data), np.std(data) #mean dan std u menghitung distribusi normal 
    x = np.linspace(min(data), max(data), 100)
    pdf = norm.pdf(x, mu, sigma) * len(data) * interval_size
    plt.plot(x, pdf, label='Kurva PDF', color='red')

    plt.xlabel('Interval Tinggi Badan')
    plt.ylabel('Frekuensi / PDF')
    plt.title('Histogram dan Kurva PDF Tinggi Badan')
    plt.legend()
    plt.show()

# Visualisasi histogram dan kurva PDF dimulai dari interval 150-160
visualisasi_histogram_dan_pdf(tinggi_badan, interval_size, start_interval=150)
