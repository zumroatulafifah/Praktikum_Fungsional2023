def perkalian(a):
    def dengan(b):
        return a*b
    return dengan

# closure mengihindari pegn var global
# fungsi yg memiliki var diluar cakupan fungsi 
#panggil dg HOF  (karna mengembalikan fungsi perkalian dan dengan) -> fungsi dalam fungsi
hasil_kali = perkalian(2)
result = hasil_kali(5)
print(result)

#currying () (fungsi dg banyak argumen diubah menjadi fungsi yg menerima 1 argum)
result = perkalian(4)(6)
print(result)