# random_list = [105, 3.1, "hello", 737, "python", 2.7, "world", 412, 5.5, "AI"]

# # Membagi elemen-elemen ke dalam tiga kategori
# data_float = list(filter(lambda x: isinstance(x, float), random_list))
# data_int = list(filter(lambda x: isinstance(x, int), random_list))
# data_string = list(filter(lambda x: isinstance(x, str), random_list))

# # Menampilkan hasil
# print("Data Float : ", tuple(data_float))
# print("Data Int : ")
# for num in data_int:
#     ratusan = num // 100
#     puluhan = (num % 100) // 10
#     satuan = num % 10
#     print({'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan})

# # print("Data String : ", [x.capitalize() for x in data_string])
# print("Data String : ", data_string)

random_list = [105, 3.1, "hello", 737, "python", 2.7, "world", 412, 5.5, "AI"]

# Membagi elemen-elemen ke dalam tiga kategori
data_float = list(filter(lambda x: isinstance(x, float), random_list))
data_int = list(filter(lambda x: isinstance(x, int), random_list))
data_string = list(filter(lambda x: isinstance(x, str), random_list))

# Menggunakan fungsi map() untuk memetakan nilai int ke satuan, puluhan, dan ratusan
def map_to_units_tens_hundreds(num):
    ratusan = num // 100
    puluhan = (num % 100) // 10
    satuan = num % 10
    return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}

data_int_mapped = list(map(map_to_units_tens_hundreds, data_int))

# Menampilkan hasil
print("Data Float : ", tuple(data_float))
print("Data Int : ", data_int_mapped)
print("Data String : ", data_string)

