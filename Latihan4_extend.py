print("\nNama: Rifka Aulia Putri")
print("NIM: 552010125015")
print("Prodi: Teknik Informatika")
print("Semester: 2")
print("Tugas: Implementasi Dictionary dan Set untuk Optimasi Data")
print("Pertemuan 10")
print("=========================")

# ==========================================
# LATIHAN 4
# Integrasi Modular + Dictionary
# ==========================================

def tambah_data(data):
    nim = input("Masukkan NIM : ").upper()

    if nim == "":
        print("NIM tidak boleh kosong.")
        return

    if nim in data:
        print("NIM sudah terdaftar.")
        return

    try:
        nilai = float(input("Masukkan Nilai : "))

        if nilai < 0 or nilai > 100:
            print("Nilai harus antara 0 - 100.")
            return

        data[nim] = nilai
        print("Data berhasil ditambahkan.")

    except ValueError:
        print("Nilai harus berupa angka.")


def tampilkan_data(data):
    if not data:
        print("Data masih kosong.")
        return

    print("\n==============================")
    print("      DATA MAHASASISWA")
    print("==============================")
    print("{:<10}{}".format("NIM", "Nilai"))
    print("------------------------------")

    for nim, nilai in data.items():
        print("{:<10}{}".format(nim, nilai))

    print("------------------------------")
    print("Jumlah Data :", len(data))


def cari_data(data):
    if not data:
        print("Data masih kosong.")
        return

    nim = input("Masukkan NIM yang dicari : ").upper()

    if nim in data:
        print("\nData ditemukan")
        print("NIM   :", nim)
        print("Nilai :", data[nim])
    else:
        print("Data tidak ditemukan.")


def jumlah_unik(data):
    if not data:
        print("Data masih kosong.")
        return

    nilai_unik = set(data.values())

    print("\n===== NILAI UNIK =====")
    print("Nilai unik :", sorted(nilai_unik))
    print("Jumlah nilai unik :", len(nilai_unik))


def menu():

    data = {}

    while True:

        print("\n===================================")
        print(" PROGRAM NILAI MAHASISWA")
        print("===================================")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Cari Data")
        print("4. Jumlah Nilai Unik")
        print("5. Keluar")
        print("===================================")

        pilih = input("Pilih menu : ")

        if pilih == "1":
            tambah_data(data)

        elif pilih == "2":
            tampilkan_data(data)

        elif pilih == "3":
            cari_data(data)

        elif pilih == "4":
            jumlah_unik(data)

        elif pilih == "5":
            print("\nTerima kasih.")
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih 1-5.")


# Program utama
if __name__ == "__main__":
    menu()