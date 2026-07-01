print("hello")
print("work in my day")
#ini comment
"""ini multi comment"""

#penamaan variabel
a=123
b=132
c=a+b
print(c)

#cara compile = python -m py_compile main.py
#cara run = python main.py
#cara run file bytecode = python main.cpython-310.pyc
#cara run file bytecode di folder __pycache__ = python __pycache__/main.cpython-310.pyc

#penamaan variabel
a = 1000
b = a
panjang = 9000

#pemanggilan variabel
print("nilai a adalah", a)
print("nilai b adalah", b)
print("nilai panjang adalah", panjang)

#penamaan variabel
nilai_y = 88 #menggunakan underscore
nilaiX = 99 #menggunakan huruf kapital
juta10 = 10000000 #menggunakan angka

#pemanggilan variabel
print("nilai y adalah", nilai_y)
print("nilai X adalah", nilaiX)
print("nilai juta10 adalah", juta10)

#penamaan variabel assignment indirect
a=6
b=a
c=a+b

#pemanggilan variabel assignment indirect
print("nilai a adalah", a)
print("nilai b adalah", b)
print("nilai c adalah", c)

#tipe data integer (tidak ada koma)
data_integer = 1000
print("data integer :", data_integer)
print("tipe data integer :", type(data_integer))

#tipe data float (ada koma)
data_float = 1000.5
print("data float :", data_float)
print("tipe data float :", type(data_float))

#tipe data string (karakter menggunakan tanda petik)
data_string = "WAHYU"
print("data string :", data_string)
print("tipe data string :", type(data_string))

#tipe data boolean (true atau false)
data_bool = True
print("data boolean :", data_bool)
print("tipe data boolean :", type(data_bool))

#tipe data complex (bilangan kompleks)
data_complex = 1 + 2j
print("data complex :", data_complex)
print("tipe data complex :", type(data_complex))

#tipe data list (daftar)
data_list = [1, 2, 3, "empat", 5.0]
print("data list :", data_list)
print("tipe data list :", type(data_list))

#data dari bahaca c
from ctypes import c_double
data_c_double = c_double(10.5)
print("data c_double :", type(data_c_double))

#CASTING DATA
#merubah tipe data

#INTEGER
print("===INTEGER===")
data_int = 9;
print("data =", data_int , ",type =", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #0 = False, selain 0 = True
print("data =", data_float , ",type =", type(data_float))
print("data =", data_str , ",type =", type(data_str))
print("data =", data_bool , ",type =", type(data_bool))

#FLOAT
print("===FLOAT===")
data_float = 9.5;
print("data =", data_float , ",type =", type(data_float))

data_int = int(data_float) #pembulatan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) #0.0 = False, selain 0.0 = True
print("data =", data_int , ",type =", type(data_int))
print("data =", data_str , ",type =", type(data_str))
print("data =", data_bool , ",type =", type(data_bool))

#BOOLEAN
print("===BOOLEAN===")
data_bool = "9";
print("data =", data_bool , ",type =",type(data_bool))

data_int = int(data_bool) #True = 1, False = 0
data_float = float(data_bool) #True = 1.0, False = 0.0
data_str = str(data_bool)
print("data =", data_int , ",type =",type(data_int))
print("data =", data_float , ",type =",type(data_float))
print("data =", data_str , ",type =",type(data_str))

#STRING
print("===STRING===")
data_str = "9";
print("data =", data_str , ",type =", type(data_str))

data_int = int(data_str) #harus angka
data_float = float(data_str) #harus angka
data_bool = bool(data_str) #"" = False, selain "" = True
print("data =", data_int , ",type =", type(data_int))
print("data =", data_float , ",type =", type(data_float))
print("data =", data_bool , ",type =", type(data_bool))

#LIST
print("===LIST===")
data_list = [1, 2, 3, "empat", 5.0]
print("data =", data_list , ",type =", type(data_list))

data_str = str(data_list) #merubah list menjadi string
data_int = int(data_list[0]) #mengambil elemen pertama dari list
data_float = float(data_list[4]) #mengambil elemen kelima dari
print("data =", data_str , ",type =", type(data_str))
print("data =", data_int , ",type =", type(data_int))
print("data =", data_float , ",type =", type(data_float))

#INPUT USER

#data yang dimasukkan pastinya string
data = input("Masukkan data: ")
print("data =", data , ",type =", type(data))

#jika ingin mengambil data integer
angka = float(input("Masukkan angka: "))
#pilih salah satu antara int atau float
angka = int(input("Masukkan angka: "))

print("angka =", angka , ",type =", type(angka))

#jika ingin mengambil data boolean
biner = bool(int(input("Masukkan nilai boolean : ")))
print("data =", biner , ",type =", type(biner))

#OPERASI ARIT MATIKA
a = 10
b = 3

#operasi tambah +
hasil = a + b
print(a,'+',b,'=',hasil)

#operasi kurang -
hasil = a - b
print(a,'-',b,'=',hasil)

#operasi kali *
hasil = a * b
print(a,'*',b,'=',hasil)

#operasi bagi /
hasil = a / b
print(a,'/',b,'=',hasil)

#operasi pangkat **
hasil = a ** b
print(a,'**',b,'=',hasil)

#operasi modulus %
hasil = a % b
print(a,'%',b,'=',hasil)

#operasi floor division //
hasil = a // b
print(a,'//',b,'=',hasil)
