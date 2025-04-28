#Nama: Willy Syifa Luthfia 
#NIM : 123140071

import math

def hitung_akar():
    while True:
        try:
            angka = input("Masukkan angka: ")
            angka = float(angka)

            if angka < 0:
                print("Input tidak valid. Harap masukkan angka positif.")
            elif angka == 0:
                print("Error: Akar kuadrat dari nol tidak diperbolehkan.")
            else:
                akar = math.sqrt(angka)
                print(f"Akar kuadrat dari {angka} adalah {akar}")
                break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka yang valid.")

# Panggil fungsi
hitung_akar()
