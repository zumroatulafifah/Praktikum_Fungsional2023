import math

def point(x, y):
    return x, y

def line_equation_of(p1, M):
    x1, y1 = p1
    C = y1 - M * x1
    return f"y = {M:.2f}x + {C:.2f}"

A = point(0, 9)
M = 0  # Gradien

# Translasi
tx = 9
ty = 9
A_translated = point(A[0] + tx, A[1] + ty) 

# Rotasi
angle = 60  # 60 derajat
x_rotated = A_translated[0] * math.cos(math.radians(angle)) - A_translated[1] * math.sin(math.radians(angle))
y_rotated = A_translated[0] * math.sin(math.radians(angle)) + A_translated[1] * math.cos(math.radians(angle))
A_rotated = point(x_rotated, y_rotated)

# Perbesaran skala
sx = 9
sy = 0
A_scaled = point(A_rotated[0] * sx, A_rotated[1] * sy)

# Menentukan persamaan garis setelah transformasi
equation_transformed = line_equation_of(A_scaled, M)

print("Persamaan garis yang melalui titik (0,9) dan bergradien 9:")
print(line_equation_of(A, M))
print("\nPersamaan garis baru setelah transformasi:")
print(equation_transformed)
