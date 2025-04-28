#Nama: Willy Syifa Luthfia
#NIM : 123140071

def tambah_tugas(tugas_list):
    tugas = input("Masukkan tugas yang ingin ditambahkan: ").strip()
    if not tugas:
        raise ValueError("Tugas tidak boleh kosong.")
    tugas_list.append(tugas)
    print("Tugas berhasil ditambahkan!")

def hapus_tugas(tugas_list):
    try:
        nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        if nomor < 1 or nomor > len(tugas_list):
            raise IndexError
        tugas_yang_dihapus = tugas_list.pop(nomor - 1)
        print(f"Tugas '{tugas_yang_dihapus}' berhasil dihapus!")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar.")
    except IndexError:
        print(f"Error: Tugas dengan nomor {nomor} tidak ditemukan.")

def tampilkan_tugas(tugas_list):
    if not tugas_list:
        print("Daftar tugas kosong.")
    else:
        print("Daftar Tugas:")
        for idx, tugas in enumerate(tugas_list, start=1):
            print(f"- {idx}. {tugas}")

def main():
    tugas_list = []

    while True:
        print("\nPilih aksi:")
        print("1. Tambah tugas")
        print("2. Hapus tugas")
        print("3. Tampilkan daftar tugas")
        print("4. Keluar")
        
        pilihan = input("Masukkan pilihan (1/2/3/4): ").strip()

        if pilihan == '1':
            try:
                tambah_tugas(tugas_list)
            except ValueError as e:
                print(f"Error: {e}")
        elif pilihan == '2':
            hapus_tugas(tugas_list)
        elif pilihan == '3':
            tampilkan_tugas(tugas_list)
        elif pilihan == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan 1, 2, 3, atau 4.")

if __name__ == "__main__":
    main()
