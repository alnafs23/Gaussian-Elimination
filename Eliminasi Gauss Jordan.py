import numpy as np

def print_matrix(matrix):
    """Fungsi untuk mencetak matriks dengan format yang rapi."""
    for row in matrix:
        print(" | ".join(f"{int(num)}" if num.is_integer() else f"{num:.2f}" for num in row))
    print()  # Tambahkan baris kosong untuk pemisah

def gauss_jordan(matrix):
    """Fungsi untuk melakukan eliminasi Gauss-Jordan."""
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
            print(" Solusi tak terhingga")
            return None  # Mengembalikan None jika tidak ada solusi

        # Normalisasi baris pivot (membuat pivot menjadi 1)
        A[i] = A[i] / pivot
        print(f"Normalisasi baris {i + 1}:")
        print_matrix(A)

        # Eliminasi elemen di atas dan di bawah pivot
        for j in range(rows):
            if j != i:  # Jangan mengubah baris pivot itu sendiri
                A[j] = A[j] - A[j, i] * A[i]
                print(f"Eliminasi baris {j + 1} menggunakan baris {i + 1}:")
                print_matrix(A)

    return A

def main():
    print("=== Program Eliminasi Gauss-Jordan ===")
    n = int(input("Masukkan jumlah variabel (baris): "))
    m = int(input("Masukkan jumlah kolom (termasuk kolom hasil): "))

    print("Masukkan elemen matriks augmented (pisahkan dengan spasi):")
    matrix = []
    for i in range(n):
        row = list(map(float, input(f"Baris {i + 1}: ").split()))
        if len(row) != m:
            print("Jumlah elemen dalam baris tidak sesuai dengan jumlah kolom.")
            return  # Keluar dari fungsi jika input tidak valid
        matrix.append(row)

    rref_matrix = gauss_jordan(matrix)

    if rref_matrix is not None:
        print("\nMatriks dalam bentuk RREF:")
        print_matrix(rref_matrix)

if __name__ == "__main__":
    main()