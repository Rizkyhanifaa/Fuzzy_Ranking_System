# Fuzzy_Ranking_System
Sistem pemeringkatan restoran di kota Bandung menggunakan metode Fuzzy Logic. Program ini membaca data dari file Excel dan menghasilkan daftar 10 restoran terbaik berdasarkan kualitas pelayanan dan harga, dengan output akhir berupa file peringkat.xlsx.

File input yang digunakan adalah:

- `restoran.xlsx`  
  Berisi data 100 restoran di Bandung dengan atribut:
  - `ID` : Nomor identitas restoran
  - `Pelayanan` : Skor pelayanan (1–100)
  - `Harga` : Harga rata-rata (Rp25.000–Rp55.000)

## 🚀 Cara Menjalankan
1. Pastikan Anda sudah menginstall Python di komputer Anda.
2. Install library yang dibutuhkan (jika belum terinstall):
    ketik pip install pandas openpyxl di terminal

3. Jalankan program melalui terminal/command prompt:
    python fuzzy.py

4. Setelah program dijalankan:
    - File `restoran.xlsx` akan dibaca
    - Sistem akan memproses data menggunakan logika fuzzy
    - File `peringkat.xlsx` akan dihasilkan di folder yang sama

Catatan:
--------
- Pastikan file `restoran.xlsx` berada di folder yang sama dengan program.
- Jangan mengubah nama kolom pada file Excel input.
