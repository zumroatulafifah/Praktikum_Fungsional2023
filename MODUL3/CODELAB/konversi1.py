def konversi(data):
    def waktu_to_menit(waktu):
        # Pisahkan waktu berdasarkan spasi
        waktu_split = waktu.split()
        menit = 0
        
        # Loop melalui setiap elemen waktu_split
        for i in range(0, len(waktu_split), 2):
            unit = waktu_split[i + 1].lower()
            if unit == 'minggu':
                menit += int(waktu_split[i]) * 7 * 24 * 60 #hari dlm seminggu jam dlm sehari menit dalam 1jam
            elif unit == 'hari':
                menit += int(waktu_split[i]) * 24 * 60
            elif unit == 'jam':
                menit += int(waktu_split[i]) * 60
            elif unit == 'menit':
                menit += int(waktu_split[i])
        
        return menit
    
    return [waktu_to_menit(waktu) for waktu in data]

data = ["3 minggu 3 hari 7 jam 21 menit", "5 minggu 5 hari 8 jam 11 menit", "7 minggu 1 hari 5 jam 33 menit"]
OutputData = konversi(data)
print ("OutputData : ", OutputData)
