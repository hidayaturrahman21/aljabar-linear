matriks_list = [
    [2, 1, -1], 
    [-3, -1, 2], 
    [-2, 1, 2]
]

print("Matriks menggunakan list:")
for new in matriks_list:
    print(new)
print('\n')

print("Indeksasi setiap elemen dalam matriks list:")
for i in range(len(matriks_list)):
    for j in range(len(matriks_list[i])):
        print(f"Elemen pada baris {i+1}, kolom {j+1} adalah {matriks_list[i][j]}")
print('\n')

import numpy as np

matriks_array = np.array([
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
])

print("Matriks menggunakan numpy array:")
print(matriks_array)
print('\n')

print("Indeksasi setiap elemen dalam matriks numpy array:")
for i in range(matriks_array.shape[0]):
    for j in range(matriks_array.shape[1]):
        print(f"Elemen pada baris {i+1}, kolom {j+1} adalah {matriks_array[i,j]}")
