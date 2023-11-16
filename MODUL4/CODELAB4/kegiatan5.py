def point(x, y):
    return x, y

def line_equation_of(p1, p2):
    def calculate_m():
        x1, y1 = p1
        x2, y2 = p2
        return (y2 - y1) / (x2 - x1)

    def calculate_c():
        x1, y1 = p1
        m = calculate_m()
        return y1 - m * x1

    M = calculate_m()
    C = calculate_c()
    return f"y = {M:.2f}x + {C:.2f}"

# Poin A dan B
A = point(1, 0)
B = point(9, 9)

# Mendapatkan persamaan garis lurus
equation_AB = line_equation_of(A, B)
print("Persamaan garis yang melalui titik A dan B:")
print(equation_AB)
