================================================================================
TUGAS ANALISIS 2: INTERAKSI ANTAR OBJEK (METHOD)
Memahami Parameter Objek pada Method
================================================================================


PERTANYAAN:
================================================================================
Perhatikan parameter lawan pada method serang. Parameter tersebut menerima 
sebuah objek utuh, bukan hanya string nama. Mengapa ini penting?


JAWABAN:
================================================================================
Parameter lawan pada method serang menerima sebuah objek utuh (bukan hanya 
string nama) karena hal ini sangat penting dalam pemrograman berorientasi 
objek. Berikut adalah alasan-alasan pentingnya:


1. SERANGAN MENGUBAH STATE, BUKAN SEKADAR MENCETAK NAMA
--------------------------------------------------------------------------------
Dalam game RPG, serangan bukan hanya menampilkan teks "Hero A menyerang Hero B", 
tetapi harus mengubah kondisi (state) dari hero yang diserang, yaitu mengurangi 
HP-nya. 

Jika parameter hanya berupa string nama:
    def serang(self, nama_lawan):
        print(f"{self.name} menyerang {nama_lawan}!")
        # Bagaimana cara mengurangi HP? Tidak bisa!

Dengan parameter objek utuh:
    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)  # Bisa memanggil method lawan!

Dengan menerima objek utuh, kita bisa mengakses method diserang() milik objek 
lawan untuk mengubah HP-nya secara langsung.


2. HANYA OBJEK YANG PUNYA DATA + PERILAKU
--------------------------------------------------------------------------------
Objek adalah gabungan dari data (atribut) dan perilaku (method). String nama 
hanya berisi data teks, tidak memiliki atribut HP, attack_power, atau method 
diserang().

Dengan objek utuh, kita bisa:
- Mengakses atribut lawan: lawan.hp, lawan.name, lawan.attack_power
- Memanggil method lawan: lawan.diserang(), lawan.info()
- Mengubah state lawan: mengurangi HP, menambah buff, dll

String nama tidak bisa melakukan hal-hal di atas.


3. MENGHINDARI KETERGANTUNGAN GLOBAL
--------------------------------------------------------------------------------
Jika parameter hanya string nama, kita harus mencari objek hero tersebut dari 
variabel global atau struktur data eksternal:

    # Cara yang buruk (dengan string nama):
    daftar_hero = {...}  # Dictionary global
    def serang(self, nama_lawan):
        lawan = daftar_hero[nama_lawan]  # Cari objek dari nama
        lawan.hp -= self.attack_power

Masalah pendekatan ini:
- Bergantung pada variabel global (daftar_hero)
- Sulit di-maintain jika ada banyak hero
- Rawan error jika nama tidak ditemukan
- Tidak fleksibel dan sulit di-test

Dengan parameter objek, method serang() berdiri sendiri tanpa ketergantungan 
eksternal:

    # Cara yang baik (dengan objek):
    def serang(self, lawan):
        lawan.diserang(self.attack_power)  # Langsung!

Method ini bisa bekerja dengan hero manapun tanpa perlu tahu struktur data di 
luar class.


4. MENDUKUNG PRINSIP ENCAPSULATION & POLYMORPHISM
--------------------------------------------------------------------------------
Encapsulation:
Dengan menerima objek, kita tidak perlu tahu detail internal bagaimana HP 
disimpan atau diubah. Kita cukup memanggil method diserang() dan biarkan objek 
lawan yang mengurus logika internalnya sendiri (validasi, enkapsulasi, dll).

    lawan.diserang(damage)  # Kita tidak peduli apakah hp private atau public

Polymorphism:
Parameter objek memungkinkan kita mengirim berbagai jenis hero (Hero, Mage, 
Assassin, dll) ke method yang sama, dan masing-masing akan merespons sesuai 
implementasinya sendiri:

    hero1.serang(hero2)     # hero2 adalah Hero biasa
    hero1.serang(eudora)    # eudora adalah Mage
    
Keduanya bekerja karena semua mewarisi class Hero dan memiliki method diserang().


5. DESAIN LEBIH BERSIH, SCALABLE, DAN PROFESIONAL
--------------------------------------------------------------------------------
Desain dengan parameter objek lebih:

Bersih (Clean):
- Tidak ada logika pencarian objek yang berbelit-belit
- Setiap method fokus pada tugasnya sendiri
- Mudah dibaca dan dipahami

Scalable (Mudah Dikembangkan):
- Mudah menambah hero baru tanpa mengubah method serang()
- Mudah menambah fitur baru (buff, critical hit, dll)
- Tidak perlu mengubah struktur data global

Profesional:
- Mengikuti best practice OOP
- Memudahkan testing dan debugging
- Code lebih maintainable untuk tim yang besar


CONTOH KONKRET:
================================================================================

Dengan String (Cara yang Salah):
```python
def serang(self, nama_lawan):
    print(f"{self.name} menyerang {nama_lawan}!")
    # Tidak bisa mengubah HP lawan!
```

Dengan Objek (Cara yang Benar):
```python
def serang(self, lawan):
    print(f"{self.name} menyerang {lawan.name}!")
    lawan.diserang(self.attack_power)
    # Bisa mengubah HP lawan melalui method-nya!
```