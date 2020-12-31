from geometri.persegipanjang import PersegiPanjang
from geometri.segitiga import SegiTiga

print('Menggunakan OOP')
p1 = PersegiPanjang(10, 3)
print(p1.info())
print(p1.hitung_luas())

s1 = SegiTiga(4, 2)
print(s1.info())
print(s1.hitung_luas())