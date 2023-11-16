import math

def translasi(tx, ty): #pergeseran
    def transformasi(p):
        x, y = p
        new_x = x + tx
        new_y = y + ty
        return new_x, new_y
    return transformasi

def dilatasi(sx, sy): #mengubah ukuran besar/kecil
    def transformasi(p):
        x, y = p
        new_x = x * sx
        new_y = y * sy
        return new_x, new_y
    return transformasi

def rotasi(sudut): #perputaran sudut
    def transformasi(p):
        x, y = p
        radian = math.radians(sudut)
        new_x = x * math.cos(radian) - y * math.sin(radian)
        new_y = x * math.sin(radian) + y * math.cos(radian)
        return new_x, new_y
    return transformasi

# Titik P awal
titik_P = (3, 5)

# Translasi
translasi_2_minus1 = translasi(2, -1)
titik_setelah_translasi = translasi_2_minus1(titik_P)
print(f"Koordinat setelah translasi: {titik_setelah_translasi}")

# Dilatasi
dilatasi_2_minus1 = dilatasi(2, -1)
titik_setelah_dilatasi = dilatasi_2_minus1(titik_P)
print(f"Koordinat setelah dilatasi: {titik_setelah_dilatasi}")

# Rotasi
rotasi_30 = rotasi(30)
titik_setelah_rotasi = rotasi_30(titik_P)
print(f"Koordinat setelah rotasi: {titik_setelah_rotasi}")

