import numpy as np

def print_matrix(matrix):
    """ Berfungsi untuk mencetak matriks dengan format yang rapi."""
    for row in matrix:
        print(" | ".join(f"{int(num)}" if num.is_integer() else f"{num:.2f}" for num in row))
    print()  

def get_augmented_matrix(rows, cols):
    """Berfungsi untuk mendapatkan matriks augmented dari input pengguna."""
    matrix = []
    print("Masukkan elemen matriks augmented dan pisahkan angka dengan spasi:")
    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"Baris {i + 1} (masukkan {cols + 1} angka): ").split()))
                if len(row) != cols + 1:
                    raise ValueError("Jumlah kolom yang diinputkan tidak sesuai.")
                matrix.append(row)
                break
            except ValueError as e:
                print(f"Input tidak valid: {e}. Silakan coba lagi.")
    return matrix

def gauss_elimination(matrix):
    """Berfungsi untuk melakukan eliminasi Gauss dan mengubah matriks menjadi REF."""
    A = np.array(matrix, dtype=float)
    rows, cols = A.shape

    print("Matriks Awal:")
    print_matrix(A)

    for i in range(rows):
        # Mencari pivot (elemen diagonal)
        pivot = A[i, i]
        
        # Jika pivot adalah 0, kita perlu menukar baris
        if pivot == 0:
            for j in range(i + 1, rows):
                if A[j, i] != 0:
                    A[[i, j]] = A[[j, i]]  # Tukar baris
                    print(f"Tukar baris {i + 1} dan baris {j + 1}:")
                    print_matrix(A)
                    pivot = A[i, i]
                    break

        # Jika setelah mencoba semua baris, pivot masih 0, sistem tidak memiliki solusi unik
        if pivot == 0:
            print("Solusi tak terhingga.")
            return None  # Mengembalikan None jika tidak ada solusi

        # Normalisasi baris pivot (membuat pivot menjadi 1)
        A[i] = A[i] / pivot
        print(f"Normalisasi baris {i + 1}:")
        print_matrix(A)

        # Eliminasi elemen di bawah pivot
        for j in range(i + 1, rows):
            A[j] = A[j] - A[j, i] * A[i]
            print(f"Eliminasi baris {j + 1} menggunakan baris {i + 1}:")
            print_matrix(A)

    return A

def back_substitution(matrix):
    """ Berfungsi untuk melakukan substitusi balik dan menyelesaikan sistem persamaan."""
    rows, cols = matrix.shape
    solution = np.zeros(rows)

    # Melakukan substitusi balik
    for i in range(rows - 1, -1, -1):
        solution[i] = matrix[i, -1]  # Mengambil nilai hasil
        for j in range(i + 1, rows):
            solution[i] -= matrix[i, j] * solution[j]  # Kurangi dengan hasil yang sudah dihitung
    return solution

def main():
    print("=== Program Eliminasi Gauss ===")
    
    while True:
        try:
            rows = int(input("Masukkan jumlah baris (variabel): "))
            cols = int(input("Masukkan jumlah kolom (koefisien): "))
            if rows <= 0 or cols <= 0:
                raise ValueError("Jumlah baris dan kolom harus positif.")
            break
        except ValueError as e:
            print(f"Input tidak valid: {e}. Silakan coba lagi.")

    matrix = get_augmented_matrix(rows, cols)

    ref_matrix = gauss_elimination(matrix)

    if ref_matrix is not None:
        print("\nMatriks dalam bentuk REF:")
        print_matrix(ref_matrix)

        solution = back_substitution(ref_matrix)
        print("Solusi untuk setiap variabel:")
        for i in range(rows):
            # Cetak solusi tanpa koma 0
            print(f"x{i + 1} = {int(solution[i]) if solution[i].is_integer() else solution[i]:.0f}")

if __name__ == "__main__":
    main()