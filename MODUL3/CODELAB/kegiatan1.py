def konversi(j=0):
    def menit(m=0):
        def detik(d=0):
            return ((j*60)+m)*60+d
        return detik
    return menit

data = "05:33:05"
data_split = data.split(':')  

print("data = ", data)
print("data split = ", data_split)

jam = int(data_split[0])
menit = int(data_split[1])
detik = int(data_split[2])
print("jam = ", jam)
print("menit = ", menit)
print("detik = ", detik)

konvert = konversi(jam)(menit)(detik)
print("Hasil Konversi = ", konvert)
