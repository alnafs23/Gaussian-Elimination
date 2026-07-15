# 🧮 Gaussian Elimination Toolkit

> Menyelesaikan Sistem Persamaan Linear (SPL) langkah demi langkah — dari matriks mentah hingga solusi akhir, tercetak transparan di setiap baris proses.

[![Python](https://img.shields.io/badge/Python-3.7%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-required-013243?logo=numpy&logoColor=white)](https://numpy.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#-lisensi)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)](#)

---

## 📖 Tentang Proyek

Repository ini berisi dua program Python interaktif berbasis CLI (*Command Line Interface*) untuk menyelesaikan **Sistem Persamaan Linear** menggunakan dua metode klasik dalam aljabar linear:

| Metode | File | Hasil Akhir |
|---|---|---|
| **Eliminasi Gauss** | `Eliminasi Gauss.py` | Row Echelon Form (REF) + substitusi balik → nilai variabel |
| **Eliminasi Gauss-Jordan** | `Eliminasi Gauss Jordan.py` | Reduced Row Echelon Form (RREF) langsung |

Keduanya dirancang bersifat **edukatif**: setiap tahap perhitungan (penukaran baris, normalisasi pivot, eliminasi) dicetak ke layar, sehingga cocok digunakan untuk belajar, mengajar, atau memverifikasi perhitungan manual mata kuliah Aljabar Linear / Metode Numerik.

---

## ✨ Fitur Utama

- 🔢 **Input matriks augmented interaktif** langsung dari terminal
- 🔄 **Penukaran baris otomatis** (*partial pivoting sederhana*) saat pivot bernilai nol
- 🧾 **Visualisasi tiap langkah** — bukan hanya hasil akhir, tapi seluruh proses transformasi matriks
- 🎯 **Deteksi sistem tanpa solusi unik** (pivot nol di seluruh baris tersisa)
- 🧮 **Substitusi balik otomatis** pada metode Gauss untuk memperoleh nilai tiap variabel
- 🧹 Output angka rapi (otomatis membulatkan tampilan bilangan bulat)

---

## 🗂️ Struktur Proyek

```
Gaussian-Elimination-main/
├── Eliminasi Gauss.py          # Metode Eliminasi Gauss + Substitusi Balik
├── Eliminasi Gauss Jordan.py   # Metode Eliminasi Gauss-Jordan (RREF)
└── README.md                   # Dokumentasi proyek
```

---

## ⚙️ Instalasi

**Prasyarat:** Python 3.7+ dan pustaka NumPy.

```bash
# 1. Clone repository
git clone https://github.com/<username>/Gaussian-Elimination.git
cd Gaussian-Elimination-main

# 2. Install dependensi
pip install numpy
```

---

## 🚀 Cara Penggunaan

### 1️⃣ Eliminasi Gauss

```bash
python "Eliminasi Gauss.py"
```

Alur input:
1. Masukkan jumlah **baris** (jumlah variabel/persamaan)
2. Masukkan jumlah **kolom** (jumlah koefisien, tanpa kolom hasil)
3. Masukkan elemen setiap baris matriks augmented, dipisah spasi

**Contoh sesi:**

```
=== Program Eliminasi Gauss ===
Masukkan jumlah baris (variabel): 3
Masukkan jumlah kolom (koefisien): 3
Masukkan elemen matriks augmented dan pisahkan angka dengan spasi:
Baris 1 (masukkan 4 angka): 2 1 -1 8
Baris 2 (masukkan 4 angka): -3 -1 2 -11
Baris 3 (masukkan 4 angka): -2 1 2 -3

... (proses eliminasi ditampilkan langkah demi langkah) ...

Matriks dalam bentuk REF:
1.00 | 0.50 | -0.50 | 4.00
0 | 1.00 | 0.25 | 3.50
0 | 0 | 1.00 | -1.00

Solusi untuk setiap variabel:
x1 = 2
x2 = 3
x3 = -1
```

### 2️⃣ Eliminasi Gauss-Jordan

```bash
python "Eliminasi Gauss Jordan.py"
```

Alur input:
1. Masukkan jumlah **variabel** (baris)
2. Masukkan jumlah **kolom** (termasuk kolom hasil/konstanta)
3. Masukkan elemen tiap baris matriks augmented

Program akan langsung menampilkan hasil akhir dalam bentuk **RREF**, tanpa perlu tahap substitusi balik.

---

## 🧠 Konsep di Balik Program

**Eliminasi Gauss** mengubah matriks menjadi *Row Echelon Form* (segitiga atas), lalu nilai variabel dicari mundur melalui **substitusi balik**.

**Eliminasi Gauss-Jordan** melanjutkan proses hingga *Reduced Row Echelon Form* — mengeliminasi elemen **di atas maupun di bawah** pivot, sehingga solusi bisa langsung dibaca dari kolom terakhir tanpa substitusi balik.

| Aspek | Gauss | Gauss-Jordan |
|---|---|---|
| Bentuk akhir | REF (segitiga atas) | RREF (diagonal identitas) |
| Eliminasi | Hanya di bawah pivot | Di atas & bawah pivot |
| Perlu substitusi balik? | ✅ Ya | ❌ Tidak |
| Kompleksitas komputasi | Sedikit lebih ringan | Sedikit lebih berat |

---

## ⚠️ Batasan Saat Ini

- Input matriks harus **persegi** (jumlah baris = jumlah variabel) agar substitusi balik dan pivot bekerja optimal
- Belum ada validasi untuk sistem yang **tak berhingga solusi** vs **tidak memiliki solusi** secara terpisah (keduanya ditangani sebagai kasus pivot nol)
- Pivoting sederhana (belum *partial pivoting* berbasis nilai absolut terbesar) — cukup untuk pembelajaran, namun kurang stabil secara numerik untuk matriks besar

---

## 🤝 Kontribusi

Kontribusi sangat terbuka! Beberapa ide pengembangan lanjutan:
- Dukungan input dari file `.csv` / `.txt`
- Mode "silent" tanpa cetak langkah demi langkah
- Partial pivoting berbasis nilai absolut maksimum
- Antarmuka grafis (GUI) atau versi web

Langkah kontribusi:
1. Fork repository ini
2. Buat branch fitur (`git checkout -b fitur-baru`)
3. Commit perubahan (`git commit -m "Menambahkan fitur X"`)
4. Push ke branch (`git push origin fitur-baru`)
5. Buka Pull Request

---

## 📄 Lisensi

Proyek ini dirilis di bawah lisensi **MIT** — bebas digunakan, dimodifikasi, dan didistribusikan untuk keperluan pembelajaran maupun pengembangan lebih lanjut.

---

<p align="center">Dibuat untuk mempermudah belajar Aljabar Linear — satu baris matriks pada satu waktu. 🧩</p>
