class Hero:
    
 # Constructor: Dijalankan saat Hero baru dibuat
 def __init__(self, name, hp, attack_power):
    self.name = name # Nama Hero
    self.hp = hp # Nyawa (Health Point)
    self.attack_power = attack_power # Kekuatan Serangan
    
 # Method untuk menampilkan info hero
 def info(self):
    print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")
    
 # Method menyerang: Objek ini (self) menyerang objek lain (lawan)
 def serang(self, lawan):
    print(f"{self.name} menyerang {lawan.name}!")
    lawan.diserang(self.attack_power)
 
 # Method diserang: Menerima damage
 def diserang(self, damage):
    self.hp -= damage
    print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")
    
 # Class Mage adalah anak dari class Hero
class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana):
        
    # Memanggil constructor milik Parent (Hero)
        super().__init__(name, hp, attack_power)
        self.mana = mana
    def info(self):
        print(f"{self.name} [Mage] | HP: {self.hp} | Mana: {self.mana}")
        
    # Mage punya skill khusus
    def skill_fireball(self, lawan):
        if self.mana >= 20:
            print(f"{self.name} menggunakan Fireball ke {lawan.name}!")
            self.mana -= 20
            lawan.diserang(self.attack_power * 2) # Damage 2x lipat
        else:
            print(f"{self.name} gagal skill! Mana tidak cukup.")
    
# -- Main Program --

# Membuat Object (Instansiasi)
hero1 = Hero("Layla", 100, 15)
hero1.hp = 500  # Mengubah atribut hp secara langsung
print(hero1.hp)  # Menampilkan atribut hp setelah diubah   
hero2 = Hero("Zilong", 120, 20)

# Memanggil Method
hero1.info()
hero2.info()

# Tambah kode Output di akhir program
print("\n--- Pertarungan Dimulai ---")
hero1.serang(hero2) # Layla menyerang Zilong
hero2.serang(hero1) # Zilong membalas    
    
# -- Main Program Baru --
print("\n--- Update Class Hero ---")
eudora = Mage("Eudora", 80, 30, 100)
balmond = Hero("Balmond", 200, 10)

eudora.info()
balmond.info()
eudora.serang(balmond) # Serangan biasa (warisan dari Hero)
eudora.skill_fireball(balmond) # Skill khusus Mage