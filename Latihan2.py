print("\nNama: Rifka Aulia Putri")
print("NIM: 552010125015")
print("Prodi: Teknik Informatika")
print("Semester: 2")
print("Tugas: Rancang cetak biru mini project")
print("Materi: CLI")
print("Pertemuan 12")
print("=========================")

data = {
    "A001": 80,
    "A002": 75,
    "A003": 90,
    "A004": 85
}

target = input("Masukkan NIM yang dicari: ")

if target in data:
    print("Nilai:", data[target])
else:
    print("Tidak ditemukan")