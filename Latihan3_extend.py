print("\nNama: Rifka Aulia Putri")
print("NIM: 552010125015")
print("Prodi: Teknik Informatika")
print("Semester: 2")
print("Tugas: Implementasi Dictionary dan Set untuk Optimasi Data")
print("Pertemuan 10")
print("=========================")

# Data awal
data = [10, 20, 20, 30, 40, 40, 50]

# Menghilangkan data duplikat
unik = set(data)

# Menampilkan hasil
print("===== DATA =====")
print("Data awal       :", data)
print("Data unik       :", sorted(unik))

print("\n===== INFORMASI =====")
print("Jumlah data awal :", len(data))
print("Jumlah data unik :", len(unik))
print("Jumlah duplikat  :", len(data) - len(unik))

# Mengecek apakah ada data duplikat
if len(data) == len(unik):
    print("Status           : Tidak ada data duplikat")
else:
    print("Status           : Ada data duplikat")