
# luasling = lambda r1, r2 : 3.14 * r1 * r2
# print(luasling(5,5))

# list = [i for i in range(20) if i % 2 == 1 ]
# print(list)

# name = ["aku" for x in range(40)]
# print(name)

my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)

print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2
# Lanjutkan hingga semua elemen diakses

def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

gen = my_generator()

for value in gen:
    print(value)
# Output: 1, 2, 3, 4, 5

