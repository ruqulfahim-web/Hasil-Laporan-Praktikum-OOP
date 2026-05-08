class Hero:
    
    # Constructor: Dijalankan saat Hero baru dibuat
    def __init__(self, name, hp, attack_power):
        self.name = name  # Nama Hero
        self.__hp = hp  # Nyawa (Health Point) - PRIVATE
        self.attack_power = attack_power  # Kekuatan Serangan
    
    # GETTER: Cara resmi melihat HP
    def get_hp(self):
        return self.__hp
    
    # SETTER: Cara resmi mengubah HP (dengan validasi)
    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0  # HP tidak boleh negatif
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dimaksimalkan ke 1000 saja.")
            self.__hp = 1000
        else:
            self.__hp = nilai_baru
    
    # Method untuk menampilkan info hero
    def info(self):
        print(f"Hero: {self.name} | HP: {self.get_hp()} | Power: {self.attack_power}")
    
    # Method menyerang: Objek ini (self) menyerang objek lain (lawan)
    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)
    
    # Method diserang: Menerima damage
    def diserang(self, damage):
        # Kita pakai setter/getter bahkan di dalam class sendiri agar aman
        sisa_hp = self.get_hp() - damage
        self.set_hp(sisa_hp)
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.get_hp()}")


# Class Mage adalah anak dari class Hero
class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana):
        # Memanggil constructor milik Parent (Hero)
        super().__init__(name, hp, attack_power)
        self.mana = mana
    
    def info(self):
        print(f"{self.name} [Mage] | HP: {self.get_hp()} | Mana: {self.mana}")
    
    # Mage punya skill khusus
    def skill_fireball(self, lawan):
        if self.mana >= 20:
            print(f"{self.name} menggunakan Fireball ke {lawan.name}!")
            self.mana -= 20
            lawan.diserang(self.attack_power * 2)  # Damage 2x lipat
        else:
            print(f"{self.name} gagal skill! Mana tidak cukup.")


print("=" * 70)
print("LATIHAN 3 & 4: INHERITANCE & ENKAPSULASI")
print("=" * 70)
print()

# -- Main Program --
# Membuat Object (Instansiasi)
hero1 = Hero("Layla", 100, 15)
hero1.set_hp(500)  # Mengubah HP dengan setter
print(hero1.get_hp())  # Menampilkan HP
hero2 = Hero("Zilong", 120, 20)

# Memanggil Method
hero1.info()
hero2.info()

# Tambah kode Output di akhir program
print("\n--- Pertarungan Dimulai ---")
hero1.serang(hero2)  # Layla menyerang Zilong
hero2.serang(hero1)  # Zilong membalas

# -- Main Program Baru --
print("\n--- Update Class Hero ---")
eudora = Mage("Eudora", 80, 30, 100)
balmond = Hero("Balmond", 200, 10)

eudora.info()
balmond.info()
eudora.serang(balmond)  # Serangan biasa (warisan dari Hero)
eudora.skill_fireball(balmond)  # Skill khusus Mage

print()
print("=" * 70)
print("UJI COBA ENKAPSULASI")
print("=" * 70)
print()

# -- Uji Coba Latihan 4 --
hero3 = Hero("Alucard", 100, 25)
hero3.set_hp(-50)  # Coba set negatif
print(f"HP setelah set -50: {hero3.get_hp()}")  # Output: 0

print(f"Mencoba akses paksa: {hero1._Hero__hp}")  # Akses atribut private (bypass)
