import random

# list ini dapat diubah sesuai kebutuhan anda.
list_nama_calket = ["Arthur", "Amuro", "Randy", "Conan", 
                    "Aji", "Sanada", "Sasuke", "Naruto", 
                    "Kuro", "Shiro", "Hanabi", "Kamikun",
                    "Shery", "Holmes", "Genta", "Kosuke",
                    "Anne", "Narukami", "Arifuru", "Maruyuma",
                    "Budialan", "Donomikizu", "Furuya", "Mai"]

ketua_terpilih = random.choice(list_nama_calket)
print(f'Selamat kepada {ketua_terpilih} yang telah terpilih dari {len(list_nama_calket)} calon ketua.')