print("\nNama: Rifka Aulia Putri")
print("NIM: 552010125015")
print("Prodi: Teknik Informatika")
print("Semester: 2")
print("Tugas: Implementasi Dictionary dan Set untuk Optimasi Data")
print("Pertemuan 10")
print("=========================")

def tambah_data(data):
    nim = input("Masukkan NIM: ")
    try:
        nilai = float(input("Masukkan nilai: "))
        data[nim] = nilai
    except ValueError:
        print("Nilai harus angka.")


def tampilkan_data(data):
    print(data)


def cari_data(data):
    nim = input("Cari NIM: ")
    if nim in data:
        print("Nilai:", data[nim])
    else:
        print("Tidak ditemukan.")


def jumlah_unik(data):
    nilai_unik = set(data.values())
    print("Jumlah nilai unik:", len(nilai_unik))


def menu():
    data = {}

    while True:
        print("\n1. Tambah")
        print("2. Tampilkan")
        print("3. Cari")
        print("4. Jumlah Nilai Unik")
        print("5. Keluar")

        pilih = input("Pilih: ")

        if pilih == "1":
            tambah_data(data)
        elif pilih == "2":
            tampilkan_data(data)
        elif pilih == "3":
            cari_data(data)
        elif pilih == "4":
            jumlah_unik(data)
        elif pilih == "5":
            break
        else:
            print("Pilihan tidak valid")


menu()