import numpy as np
import matplotlib.pyplot as plt
import sympy as sp 

# Soal 1 dengan NumPy
A = np.array([[2, 3], [1, -1]])
b = np.array([7, 1])
solusi_1 = np.linalg.solve(A, b)
print(f"Solusi soal 1 dengan NumPy = x: {solusi_1[0]:.2f} y: {solusi_1[1]:.2f}")

# Grafik soal 1 dengan NumPy
x_vals = np.linspace(-5, 5, 100)
y1_vals = (7 - 2 * x_vals) / 3
y2_vals = x_vals - 1
plt.figure(figsize=(8,6))
plt.plot(x_vals, y1_vals, label="2x + 3y = 7", color="blue")
plt.plot(x_vals, y2_vals, label="x - y = 1", color="green")
plt.scatter(solusi_1[0], solusi_1[1], color="red", label=f"Solusi: ({solusi_1[0]:.2f}, {solusi_1[1]:.2f})")
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title("Diagram Soal 1 dengan NumPy")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

# Soal 1 dengan SymPy
x, y = sp.symbols('x y')
persamaan1 = sp.Eq(2*x + 3*y, 7)
persamaan2 = sp.Eq(x - y, 1)
solusi_2 = sp.solve((persamaan1, persamaan2), (x, y))
print(f"Solusi soal 1 dengan SymPy = {solusi_2}")

# Grafik soal 1 dengan SymPy (menggunakan kembali x_vals dan y_vals dari NumPy)
plt.figure(figsize=(8,6))
plt.plot(x_vals, y1_vals, label="2x + 3y = 7", color="blue")
plt.plot(x_vals, y2_vals, label="x - y = 1", color="green")
if isinstance(solusi_2, dict):
    plt.scatter(float(solusi_2[x]), float(solusi_2[y]), color="red", label=f"Solusi: ({float(solusi_2[x]):.2f}, {float(solusi_2[y]):.2f})")
else:
    print("SymPy solve tidak mengembalikan solusi dictionary yang valid untuk sistem 2D.")
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.title("Diagram Soal 1 dengan SymPy")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

# Soal 2 dengan NumPy
Matriks_A = np.array([[1, 2, 1], [3, -1, 2], [-2, 3, -1]])
Matriks_B = np.array([10, 5, -9])
solusi_3 = np.linalg.solve(Matriks_A, Matriks_B)
print(f"Solusi soal 2 dengan NumPy = x: {solusi_3[0]:.2f}, y: {solusi_3[1]:.2f}, z: {solusi_3[2]:.2f}")

# Grafik soal 2 dengan NumPy (Visualisasi 3D)
x_vals_3d = np.linspace(-10, 10, 50) # Menggunakan titik yang lebih sedikit untuk meshgrid 3D
y_vals_3d = np.linspace(-10, 10, 50)
X, Y = np.meshgrid(x_vals_3d, y_vals_3d)

# Definisikan fungsi untuk setiap bidang
Z1 = (10 - X - 2 * Y)
Z2 = (5 - 3 * X + Y) / 2
Z3 = (-9 + 2 * X - 3 * Y)

fig = plt.figure(figsize=(10, 7))
# Matplotlib secara otomatis akan menggunakan proyeksi 3D jika argumen projection='3d' ada
ax = fig.add_subplot(111, projection='3d')

# Plot permukaan bidang-bidang
ax.plot_surface(X, Y, Z1, alpha=0.5, color='blue', label="1x + 2y + 1z = 10")
ax.plot_surface(X, Y, Z2, alpha=0.5, color='green', label="3x - 1y + 2z = 5")
ax.plot_surface(X, Y, Z3, alpha=0.5, color='red', label="-2x + 3y - 1z = -9")

# Plot titik solusi menggunakan hasil NumPy
ax.scatter(solusi_3[0], solusi_3[1], solusi_3[2], color="black", s=50, label=f"Solusi (NumPy): ({solusi_3[0]:.2f}, {solusi_3[1]:.2f}, {solusi_3[2]:.2f})")

ax.set_title("Visualisasi Soal 2 dalam 3D (NumPy)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
# Legenda untuk scatter plot akan muncul
plt.legend()
plt.show()

# Soal 2 dengan SymPy
x_sp, y_sp, z_sp = sp.symbols('x y z') # Gunakan nama variabel yang berbeda untuk symbol SymPy di bagian ini
persamaan1_sp = sp.Eq(x_sp + 2*y_sp + z_sp, 10)
persamaan2_sp = sp.Eq(3*x_sp - y_sp + 2*z_sp, 5)
persamaan3_sp = sp.Eq(-2*x_sp + 3*y_sp - z_sp, -9)

# Solusi SymPy untuk sistem 3D
solusi_sympy_3d = sp.solve((persamaan1_sp, persamaan2_sp, persamaan3_sp), (x_sp, y_sp, z_sp))
print(f"Solusi soal 2 dengan SymPy = {solusi_sympy_3d}")

# Grafik 3D lainnya (menggunakan solusi SymPy)
# Menggunakan kembali X, Y, Z1, Z2, Z3 dari meshgrid dan fungsi bidang di atas

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot kembali bidang-bidang (menggunakan label untuk tujuan deskriptif di plot)
ax.plot_surface(X, Y, Z1, alpha=0.5, color='red', label='x + 2y + z = 10')
ax.plot_surface(X, Y, Z2, alpha=0.5, color='green', label='3x - y + 2z = 5')
ax.plot_surface(X, Y, Z3, alpha=0.5, color='blue', label='-2x + 3y - z = -9')

# Plot titik solusi menggunakan hasil SymPy (dictionary)
# Periksa apakah solusi adalah dictionary dan tidak kosong
if isinstance(solusi_sympy_3d, dict) and solusi_sympy_3d:
    # Akses nilai solusi menggunakan simbol SymPy sebagai kunci dan ubah ke float
    ax.scatter(float(solusi_sympy_3d[x_sp]), float(solusi_sympy_3d[y_sp]), float(solusi_sympy_3d[z_sp]),
               color="black", s=50,
               label=f"Solusi (SymPy): ({float(solusi_sympy_3d[x_sp]):.2f}, {float(solusi_sympy_3d[y_sp]):.2f}, {float(solusi_sympy_3d[z_sp]):.2f})")
else:
    print("SymPy solve tidak mengembalikan solusi dictionary yang valid untuk sistem 3D (plot).")

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Visualisasi Tiga Bidang dari Sistem Linear (SymPy Solution)')

# Legenda untuk scatter plot akan muncul
plt.legend()
plt.show()
