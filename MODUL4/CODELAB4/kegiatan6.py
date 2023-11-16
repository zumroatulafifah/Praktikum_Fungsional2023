def point(x, y):
    return x, y

def line_equation_of(p1, M):
    x1, y1 = p1
    C = y1 - M * x1  # Menghitung nilai ||  y-y1 = m(x-x1) || dikali pelangi 
    return f"y = {M:.2f}x + {C:.2f}"

print("Persamaan garis yang melalui titik (0, 9) dan bergradien 9 :")
print(line_equation_of((0, 9), 9))
