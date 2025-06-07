# membuat matriks menggunakan list
print('-'*65)
matriks_list = ([ 2,  1, -1],
                [-3, -1,  2],
                [-2,  1,  2])

print ("ini adalah matriks dari List:")
for list in matriks_list:
    print(list)

print('-'*65)
print("Elemen Baris Pertama Kolom Pertama dari Matriks List adalah : ",matriks_list[0][0])

print("Elemen Baris Kedua   Kolom Pertama dari Matriks List adalah :", matriks_list[1][0])

print("Elemen Baris Ketiga  Kolom Pertama dari Matriks List adalah :", matriks_list[2][0])

print('-'*65)
print("Elemen Baris Pertama Kolom Kedua   dari Matriks List adalah : ",matriks_list[0][1])

print("Elemen Baris Kedua   Kolom Kedua   dari Matriks List adalah :", matriks_list[1][1])

print("Elemen Baris Ketiga  Kolom Kedua   dari Matriks List adalah : ",matriks_list[2][1])

print('-'*65)
print("Elemen Baris Pertama Kolom Ketiga  dari Matriks List adalah :", matriks_list[0][2])

print("Elemen Baris Kedua   Kolom Ketiga  dari Matriks List adalah : ",matriks_list[1][2])

print("Elemen Baris Ketiga  Kolom Ketiga  dari Matriks List adalah : ",matriks_list[2][2])
print('-'*65)

import numpy as np
# Membuat matriks menggunakan Array
matriks_array = ([[2, 1, -1], 
                  [-3,-1, 2],
                  [-2, 1, 2]])
print("ini adalah matriks dari Array:")
print(matriks_array)

print("-"*65)
print("Elemen Baris Pertama Kolom Pertama dari Matriks Array adalah : ",matriks_array[0][0])

print("Elemen Baris Kedua   Kolom Pertama dari Matriks Array adalah :", matriks_array[1][0])

print("Elemen Baris Ketiga  Kolom Pertama dari Matriks Array adalah :", matriks_array[2][0])
print("-"*65)
print("Elemen Baris Pertama Kolom Kedua   dari Matriks Array adalah : ",matriks_array[0][1])

print("Elemen Baris Kedua   Kolom Kedua   dari Matriks Array adalah :", matriks_array[1][1])

print("Elemen Baris Ketiga  Kolom Kedua   dari Matriks Array adalah : ",matriks_array[2][1])

print("-"*65)
print("Elemen Baris pertama Kolom Ketiga  dari Matriks Array adalah :", matriks_array[0][2])

print("Elemen Baris Kedua   Kolom Ketiga  dari Matriks Array adalah : ",matriks_array[1][2])

print("Elemen Baris Ketiga  Kolom Ketiga  dari Matriks Array adalah : ",matriks_array[2][2])
print("-"*65)
