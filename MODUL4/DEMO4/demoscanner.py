import math

def point(x, y):
    return x, y

def line_equation_of(p1, M):
    x1, y1 = p1
    C = y1 - M * x1
    return f"y = {M:.2f}x + {C:.2f}"

# Decorator untuk transformasi gabungan
def combined_transform(*func_list):
    def decorator(p):
        for transform_func in func_list:
            p = transform_func(p)
        return p
    return decorator

# Fungsi decorator dengan simbol "@"
@combined_transform
def translate(p): #pergeseran
    x, y = p
    return point(x + 9, y + 9)

@combined_transform
def rotate(p): #perputaran
    x, y = p
    x_rotated = x * math.cos(math.radians(60)) - y * math.sin(math.radians(60))
    y_rotated = x * math.sin(math.radians(60)) + y * math.cos(math.radians(60))
    return point(x_rotated, y_rotated)

@combined_transform
def scale(p): #perbesaran skala 
    x, y = p
    return point(x * 9, y * 0)  # Mengubah faktor skala y menjadi 9

# Input titik dari pengguna
x_input = float(input("Masukkan nilai x untuk titik A: "))
y_input = float(input("Masukkan nilai y untuk titik A: "))
A = point(x_input, y_input)

# Gradien
M = 0

# Menggunakan decorator pada titik A
A_transformed = scale(rotate(translate(A)))

# Menentukan persamaan garis setelah transformasi
equation_transformed = line_equation_of(A_transformed, M)

print("Persamaan garis yang melalui titik A dan bergradien 0:")
print(line_equation_of(A, M))
print("\nPersamaan garis baru setelah transformasi:")
print(equation_transformed)
