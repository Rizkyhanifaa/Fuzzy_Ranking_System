# Untuk mengekstrak data dari file Excel restoran.xlsx
import pandas as pd

# 1. Fungsi keanggotaan (Pelayanan)
def pel_buruk(x):
    if x <= 30: return 1
    if x <= 50: return (50 - x) / 20
    return 0

def pel_sedang(x):
    if x <= 30 or x >= 70: return 0
    if x <= 50: return (x - 30) / 20
    return (70 - x) / 20

def pel_baik(x):
    if x <= 50: return 0
    if x <= 70: return (x - 50) / 20
    return 1

# 2. Fungsi keanggotaan (Harga)
def hr_murah(x):
    if x <= 30000: return 1
    if x <= 35000: return (35000 - x) / 5000
    return 0

def hr_sedang(x):
    if x <= 30000 or x >= 50000: return 0
    if x <= 40000: return (x - 30000) / 10000
    return (50000 - x) / 10000

def hr_mahal(x):
    if x <= 45000: return 0
    if x <= 50000: return (x - 45000) / 5000
    return 1

# 3. Rule base + defuzzification (height method)
RULES = [
    (pel_baik,   hr_murah,  90),
    (pel_baik,   hr_sedang, 75),
    (pel_baik,   hr_mahal,  60),
    (pel_sedang, hr_murah,  75),
    (pel_sedang, hr_sedang, 60),
    (pel_sedang, hr_mahal,  40),
    (pel_buruk,  hr_murah,  60),
    (pel_buruk,  hr_sedang, 40),
    (pel_buruk,  hr_mahal,  20),
]

def eval_fuzzy(p, h):
    numer = denom = 0.0
    for pel_f, hr_f, out_val in RULES:
        deg = min(pel_f(p), hr_f(h))
        numer += deg * out_val
        denom += deg
    return (numer / denom) if denom != 0 else 0

def main():
    # 4. Baca & bersihkan header Excel
    df = pd.read_excel('restoran.xlsx')
    df.columns = [c.strip().title() for c in df.columns]
    first_col = df.columns[0]
    if first_col.lower().startswith('id'):
        df = df.rename(columns={first_col: 'ID'})
    
    expected = {'ID', 'Pelayanan', 'Harga'}
    if not expected.issubset(set(df.columns[:3])):
        raise KeyError(f"Header tidak sesuai: {df.columns.tolist()}")

    # 5. Hitung skor fuzzy dan kategorisasi
    results = []
    for _, row in df.iterrows():
        idx = row['ID']
        pel = row['Pelayanan']
        hr  = row['Harga']
        score = eval_fuzzy(pel, hr)
        mu_p = {'Buruk': pel_buruk(pel), 'Sedang': pel_sedang(pel), 'Baik': pel_baik(pel)}
        kat_p = max(mu_p, key=mu_p.get)
        results.append((idx, score, kat_p, hr))

    # 6. Urutkan & ambil Top-10 dan Top-5
    results.sort(key=lambda x: x[1], reverse=True)
    top10 = results[:10]
    top5 = results[:5]

    # 7. Cetak Top-10 ke terminal
    print("10 Restoran Terbaik di Kota Bandung:")
    print("ID\tSkor\tPelayanan\tHarga")
    for r in top10:
        print(f"{r[0]}\t{r[1]:.2f}\t{r[2]}\t\t{r[3]}")

    # 8. Simpan Top-5 ke Excel
    out_df = pd.DataFrame(top5, columns=['ID_Restoran','Skor','Kualitas Pelayanan','Harga'])
    out_df.to_excel('peringkat.xlsx', index=False)

    print("\nFile 'peringkat.xlsx' berhasil dibuat dengan Top-5 restoran.")

if __name__ == '__main__':
    main()
