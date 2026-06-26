print("\nNama: Rifka Aulia Putri")
print("NIM: 552010125015")
print("Prodi: Teknik Informatika")
print("Semester: 2")
print("Tugas: Rancang cetak biru mini project")
print("Materi: CLI")
print("Pertemuan 12")
print("=========================")

data = ["A001", "A002", "A003", "A004"]

target = input("Masukkan NIM yang dicari: ")

count = 0
found = False

for item in data:
    count += 1
    if item == target:
        found = True
        break

print("Ditemukan:", found)
print("Jumlah langkah:", count)