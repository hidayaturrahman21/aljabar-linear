import numpy as np

# Matriks P dan Q
P = np.array([
    [11, 12, 13],
    [14, 15, 16],
    [17, 18, 19]
])

Q = np.array([
    [20, 21, 22],
    [23, 24, 25],
    [26, 27, 28]
])

# 1. Penjumlahan
penjumlahan = P + Q

# 2. Pengurangan
pengurangan = P - Q

# 3. Perkalian Dot (Matrix multiplication)
perkalian_dot = np.dot(P, Q)

# 4. Perkalian Cross dari baris pertama P dan Q
cross_product = np.cross(P[0], Q[0])

# 5. Transpose
transpose_P = P.T
transpose_Q = Q.T

# Cetak hasil
print("Matriks P:")
print(P)
print("\nMatriks Q:")
print(Q)

print("\n1. Penjumlahan (P + Q):")
print(penjumlahan)

print("\n2. Pengurangan (P - Q):")
print(pengurangan)

print("\n3. Perkalian Dot (P @ Q):")
print(perkalian_dot)

print("\n4. Cross Product (baris pertama P x Q):")
print(cross_product)

print("\n5. Transpose P:")
print(transpose_P)

print("\n6. Transpose Q:")
print(transpose_Q)
