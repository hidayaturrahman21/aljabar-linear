import numpy as np

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
penjumlahan = P + Q
pengurangan = P - Q

perkalian_dot = np.dot(P, Q)
cross_product = np.cross(P[0], Q[0])

transpose_P = P.T
transpose_Q = Q.T

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
