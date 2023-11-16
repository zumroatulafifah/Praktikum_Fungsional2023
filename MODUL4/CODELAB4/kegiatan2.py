def uppercase_decorator(function):
    def wrapper():
        func = function()
        #make uppercase = func.upper()
        return func.upper()
    return wrapper

# mengubah atau memodifikasi fungsi tanpa mengubah kode sumber asli dari fungsi tersebut
@uppercase_decorator
def say_hi():
    return 'hello there'
result = say_hi()
print(result)

# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         # Membuat teks menjadi huruf besar
#         func = func.upper()
#         return func
#     return wrapper

# # Contoh penggunaan decorator
# @uppercase_decorator
# def greet():
#     return "hello, world!"

# # Memanggil fungsi yang telah di-decorate
# result = greet()
# print(result)
