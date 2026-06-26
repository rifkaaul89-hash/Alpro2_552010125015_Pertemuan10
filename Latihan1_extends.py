print("\nNama: Rifka Aulia Putri")
print("NIM: 552010125015")
print("Prodi: Teknik Informatika")
print("Semester: 2")
print("Tugas: Rancang cetak biru mini project")
print("Materi: CLI")
print("Pertemuan 12")
print("=========================")

# Data NIM mahasiswa
data = ["A001", "A002", "A003", "A004"]

# Menampilkan daftar NIM
print("===== DAFTAR NIM =====")
for nim in data:
    print("-", nim)

# Input NIM yang dicari
target = input("\nMasukkan NIM yang dicari: ").upper()

count = 0
found = False
posisi = -1

# Proses pencarian
for i in range(len(data)):
    count += 1

    if data[i] == target:
        found = True
        posisi = i
        break

# Output hasil pencarian
print("\n===== HASIL PENCARIAN =====")

if found:
    print("Status          : Ditemukan")
    print("NIM             :", target)
    print("Posisi Data     :", posisi + 1)
else:
    print("Status          : Tidak ditemukan")

print("Jumlah langkah  :", count)