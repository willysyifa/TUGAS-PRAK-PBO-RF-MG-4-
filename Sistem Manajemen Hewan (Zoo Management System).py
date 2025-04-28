#Nama: Willy Syifa Luthfia
#NIM : 123140071

from abc import ABC, abstractmethod

# Abstraction
class Animal(ABC):
    def __init__(self, name, age):
        self.__name = name    # Encapsulation
        self.__age = age

    @abstractmethod
    def make_sound(self):
        pass

    # Getter and Setter untuk name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        if not name:
            raise ValueError("Nama tidak boleh kosong.")
        self.__name = name

    # Getter and Setter untuk age
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age <= 0:
            raise ValueError("Usia harus lebih dari 0.")
        self.__age = age

# Inheritance + Polymorphism
class Dog(Animal):
    def make_sound(self):
        return "Guk Guk!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Bird(Animal):
    def make_sound(self):
        return "Cuit Cuit!"

class Zoo:
    def __init__(self):
        self.__animals = []

    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError("Yang ditambahkan harus objek Animal.")
        self.__animals.append(animal)
        print(f"Hewan {animal.get_name()} berhasil ditambahkan!")

    def show_animals(self):
        if not self.__animals:
            print("Kebun binatang kosong.")
        else:
            print("\nDaftar Hewan di Kebun Binatang:")
            for idx, animal in enumerate(self.__animals, 1):
                print(f"{idx}. {animal.get_name()} (Umur: {animal.get_age()} tahun) - Suara: {animal.make_sound()}")

def main():
    zoo = Zoo()

    while True:
        print("\n=== Sistem Manajemen Hewan ===")
        print("1. Tambah Hewan")
        print("2. Tampilkan Daftar Hewan")
        print("3. Keluar")
        
        pilihan = input("Masukkan pilihan (1/2/3): ").strip()

        if pilihan == '1':
            try:
                name = input("Masukkan nama hewan: ").strip()
                if not name:
                    raise ValueError("Nama tidak boleh kosong.")
                age = int(input("Masukkan umur hewan: "))
                if age <= 0:
                    raise ValueError("Usia harus lebih dari 0.")

                print("Pilih jenis hewan:")
                print("1. Anjing")
                print("2. Kucing")
                print("3. Burung")
                jenis = input("Masukkan pilihan jenis (1/2/3): ").strip()

                if jenis == '1':
                    animal = Dog(name, age)
                elif jenis == '2':
                    animal = Cat(name, age)
                elif jenis == '3':
                    animal = Bird(name, age)
                else:
                    raise ValueError("Jenis hewan tidak valid.")

                zoo.add_animal(animal)

            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Terjadi kesalahan: {e}")

        elif pilihan == '2':
            zoo.show_animals()

        elif pilihan == '3':
            print("Keluar dari sistem. Sampai jumpa!")
            break

        else:
            print("Pilihan tidak valid. Masukkan 1, 2, atau 3.")

if __name__ == "__main__":
    main()
