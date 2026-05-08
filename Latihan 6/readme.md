================================================================================
TUGAS ANALISIS 6: POLYMORPHISM (FLEKSIBILITAS INTERAKSI)
================================================================================


PERTANYAAN 1: UJI SKALABILITAS (KEMUDAHAN MENAMBAH FITUR)
================================================================================
Tanpa mengubah satu huruf pun pada kode Looping (for pahlawan in pasukan:), 
buatlah satu class baru bernama Healer(Hero).

Isi method serang milik Healer dengan: 
print(f"{self.nama} tidak menyerang, tapi menyembuhkan teman!")

Masukkan objek Healer ke dalam list pasukan.

a) Pertanyaan: Apakah program berjalan lancar?
b) Kesimpulannya, apa keuntungan Polimorfisme bagi seorang programmer ketika 
   harus mengupdate game dengan karakter baru di masa depan?


JAWABAN:
================================================================================

a) Apakah Program Berjalan Lancar?
-----------------------------------
Ya, program berjalan dengan SANGAT LANCAR tanpa error sama sekali!

Berikut kode yang ditambahkan:

```python
# Class baru Healer (ditambahkan setelah class Fighter)
class Healer(Hero):
    def serang(self):
        print(f"{self.nama} tidak menyerang, tapi menyembuhkan teman!")

# Menambahkan Healer ke dalam list pasukan
pasukan = [
    Mage("Eudora"),
    Archer("Miya"),
    Fighter("Zilong"),
    Mage("Gord"),
    Healer("Estes")  # Objek baru ditambahkan
]

print("--- PERANG DIMULAI ---")
# Loop yang SAMA PERSIS, tidak diubah satu huruf pun
for pahlawan in pasukan:
    pahlawan.serang()
```

Output yang dihasilkan:
```
--- PERANG DIMULAI ---
Eudora (Mage) menembakkan Bola Api! Boom!
Miya (Archer) memanah dari jauh! Jleb!
Zilong (Fighter) memukul dengan pedang! Slash!
Gord (Mage) menembakkan Bola Api! Boom!
Estes tidak menyerang, tapi menyembuhkan teman!
```

Program berjalan lancar karena:
1. Class Healer mewarisi dari Hero
2. Healer memiliki method serang() (override dari parent)
3. Loop for tidak peduli jenis hero apa yang ada di list
4. Loop hanya memanggil method serang() - semua hero punya method ini


b) Kesimpulan: Keuntungan Polimorfisme untuk Programmer
--------------------------------------------------------
Polimorfisme memberikan BANYAK KEUNTUNGAN ketika harus mengupdate game dengan 
karakter baru di masa depan:

1. TIDAK PERLU MENGUBAH KODE YANG SUDAH ADA
   Ketika menambahkan hero baru (Healer), kita TIDAK perlu mengubah:
   - Kode loop yang sudah ada
   - Logic pertempuran yang sudah ada
   - Fungsi-fungsi lain yang menggunakan hero
   
   Ini sangat menghemat waktu dan mengurangi risiko merusak kode yang sudah 
   bekerja dengan baik.

2. MUDAH MENAMBAH FITUR BARU (SCALABLE)
   Untuk menambah karakter baru, programmer hanya perlu:
   - Buat class baru yang mewarisi Hero
   - Override method serang() dengan perilaku unik
   - Tambahkan objek ke list pasukan
   
   Hanya 3 langkah sederhana! Tidak perlu menulis ulang sistem pertempuran.

3. KODE LEBIH FLEKSIBEL DAN ADAPTIF
   Satu kode loop yang sama bisa menangani:
   - Hero tipe lama (Mage, Archer, Fighter)
   - Hero tipe baru (Healer, Tank, Assassin, dll)
   - Berapa pun jumlah tipe hero yang akan dibuat di masa depan
   
   Loop tidak perlu tahu detail masing-masing hero, cukup panggil serang().

4. MENGURANGI DUPLIKASI KODE (DRY PRINCIPLE)
   Tanpa Polymorphism, kita harus menulis:
   ```python
   for hero in pasukan:
       if isinstance(hero, Mage):
           hero.lempar_bola_api()
       elif isinstance(hero, Archer):
           hero.tembak_panah()
       elif isinstance(hero, Fighter):
           hero.pukul_pedang()
       elif isinstance(hero, Healer):
           hero.sembuhkan()
       # Harus tambah elif setiap kali ada hero baru!
   ```
   
   Dengan Polymorphism, cukup:
   ```python
   for hero in pasukan:
       hero.serang()  # Otomatis memanggil method yang sesuai!
   ```

5. MEMUDAHKAN TIM DEVELOPMENT
   Dalam tim besar:
   - Programmer A mengerjakan sistem pertempuran (loop)
   - Programmer B, C, D bisa menambahkan hero baru secara bersamaan
   - Tidak ada konflik kode karena masing-masing hanya menambah class baru
   - Tidak perlu koordinasi rumit untuk update kode yang sudah ada

6. MENGURANGI BUG DAN ERROR
   Karena kode lama tidak diubah, kemungkinan merusak fitur yang sudah bekerja 
   menjadi sangat kecil. Setiap penambahan hero baru tidak akan mempengaruhi 
   hero yang sudah ada.

7. KODE LEBIH MUDAH DI-MAINTAIN
   6 bulan kemudian ketika programmer lain membaca kode, mereka langsung paham:
   "Oh, untuk menambah hero baru, tinggal buat class yang mewarisi Hero dan 
   override method serang(). Gampang!"
   
   Strukturnya jelas dan konsisten.

8. MENDUKUNG OPEN-CLOSED PRINCIPLE
   Salah satu prinsip SOLID dalam software engineering:
   - Open for extension: Mudah menambah fitur baru (hero baru)
   - Closed for modification: Tidak perlu mengubah kode yang sudah ada
   
   Ini adalah tanda kode yang berkualitas tinggi.


Analogi Dunia Nyata:
--------------------
Bayangkan kamu punya remote TV universal:
- Remote (loop) tidak peduli merk TV apa yang kamu punya
- Remote hanya punya tombol "Power", "Volume", "Channel"
- TV baru apapun yang kamu beli nanti, remote tetap bisa dipakai
- Tidak perlu ganti remote atau modifikasi remote setiap beli TV baru

Itulah Polymorphism: satu interface (method serang) bisa bekerja dengan banyak 
implementasi berbeda (Mage, Archer, Fighter, Healer, dll).


KESIMPULAN PERTANYAAN 1:
-------------------------
Program berjalan lancar tanpa masalah. Keuntungan Polymorphism adalah:
1. Tidak perlu ubah kode yang sudah ada
2. Mudah menambah fitur baru (scalable)
3. Kode lebih fleksibel dan adaptif
4. Mengurangi duplikasi kode
5. Memudahkan kolaborasi tim
6. Mengurangi bug
7. Mudah di-maintain
8. Mengikuti prinsip SOLID

Dengan Polymorphism, game dapat berkembang dan bertambah fiturnya tanpa harus 
menulis ulang atau merusak sistem yang sudah ada.


================================================================================


PERTANYAAN 2: KONSISTENSI PENAMAAN
================================================================================
Ubah nama method serang pada class Archer menjadi tembak_panah. 
Jalankan program.

a) Pertanyaan: Apa yang terjadi?
b) Mengapa dalam konsep Polimorfisme, nama method antara Parent Class dan 
   berbagai Child Class harus persis sama?


JAWABAN:
================================================================================

a) Apa yang Terjadi?
--------------------
Ketika kita mengubah nama method serang() menjadi tembak_panah() pada class 
Archer:

```python
class Archer(Hero):
    def tembak_panah(self):  # SALAH! Harusnya serang()
        print(f"{self.nama} (Archer) memanah dari jauh! Jleb!")
```

Lalu menjalankan program, yang terjadi adalah:

**ERROR! Program CRASH!**

Error yang muncul:
```
--- PERANG DIMULAI ---
Eudora (Mage) menembakkan Bola Api! Boom!
Hero menyerang dengan tangan kosong.
Zilong (Fighter) memukul dengan pedang! Slash!
Gord (Mage) menembakkan Bola Api! Boom!
```

Atau bisa juga muncul:
```
AttributeError: 'Archer' object has no attribute 'serang'
```

Penjelasan yang terjadi:
1. Loop memanggil pahlawan.serang() untuk semua hero
2. Saat giliran Archer (Miya), loop mencari method serang()
3. Class Archer TIDAK PUNYA method serang() (sudah diganti jadi tembak_panah)
4. Python mencari di parent class Hero, menemukan method serang() yang default
5. Yang dipanggil adalah method serang() dari parent (Hero), bukan dari Archer
6. Output jadi: "Hero menyerang dengan tangan kosong." (bukan panah!)

Atau jika parent class Hero tidak punya default implementation, program akan 
langsung error dan crash.


b) Mengapa Nama Method Harus Persis Sama?
------------------------------------------
Dalam konsep Polimorfisme, nama method antara Parent Class dan Child Class HARUS 
PERSIS SAMA karena alasan-alasan berikut:

1. POLYMORPHISM BERGANTUNG PADA KONSISTENSI NAMA
   Polymorphism bekerja dengan prinsip: "Satu nama method, banyak implementasi."
   
   Jika namanya beda:
   - Bukan Polymorphism lagi, tapi method yang berbeda total
   - Python tidak tahu kalau tembak_panah() seharusnya menggantikan serang()
   - Programmer harus tahu detail setiap class (melanggar prinsip abstraksi)

2. LOOP/FUNGSI UMUM TIDAK BISA BEKERJA
   Loop seperti ini:
   ```python
   for pahlawan in pasukan:
       pahlawan.serang()
   ```
   
   Mengharapkan SEMUA objek dalam list punya method serang().
   
   Jika Archer punya tembak_panah() bukan serang():
   - Loop tidak tahu harus memanggil method apa untuk Archer
   - Loop tidak bisa otomatis menyesuaikan nama method per objek
   - Polymorphism rusak total

3. INTERFACE/KONTRAK DILANGGAR
   Parent class (Hero) bertindak sebagai "kontrak" yang menyatakan:
   "Semua hero HARUS punya method serang()."
   
   Jika Child class (Archer) menggunakan nama lain (tembak_panah):
   - Kontrak dilanggar
   - Tidak ada jaminan semua hero bisa diperlakukan sama
   - Kode jadi tidak konsisten dan sulit diprediksi

4. DYNAMIC DISPATCH TIDAK BERFUNGSI
   Python menggunakan mekanisme "dynamic dispatch" untuk Polymorphism:
   - Saat runtime, Python mencari method dengan nama yang SAMA di class objek
   - Jika nama beda, Python tidak akan menemukan method yang sesuai
   - Yang dipanggil adalah method parent (atau error jika tidak ada)

5. TIDAK ADA CARA OTOMATIS MAPPING NAMA BERBEDA
   Python tidak punya cara untuk tahu bahwa:
   - serang() untuk Mage = lempar_bola_api()
   - serang() untuk Archer = tembak_panah()
   - serang() untuk Fighter = pukul_pedang()
   
   Programmer harus menulis nama method yang SAMA agar Python bisa otomatis 
   memanggil implementasi yang tepat untuk setiap objek.

6. KODE JADI RUMIT DAN TIDAK SCALABLE
   Jika setiap class boleh pakai nama method sendiri, kita harus menulis:
   
   ```python
   for hero in pasukan:
       if isinstance(hero, Mage):
           hero.lempar_bola_api()
       elif isinstance(hero, Archer):
           hero.tembak_panah()
       elif isinstance(hero, Fighter):
           hero.pukul_pedang()
       elif isinstance(hero, Healer):
           hero.sembuhkan()
       # Harus tambah terus setiap ada hero baru!
   ```
   
   Ini bertentangan dengan tujuan Polymorphism: satu kode untuk semua tipe.

7. OVERRIDE METHOD TIDAK TERJADI
   Override adalah mengganti implementasi method parent dengan implementasi 
   child. Agar override terjadi, nama method HARUS SAMA PERSIS:
   
   Benar (Override):
   ```python
   class Parent:
       def serang(self):
           pass
   
   class Child(Parent):
       def serang(self):  # OVERRIDE! Nama sama
           pass
   ```
   
   Salah (Bukan Override):
   ```python
   class Parent:
       def serang(self):
           pass
   
   class Child(Parent):
       def tembak_panah(self):  # BUKAN OVERRIDE! Nama beda
           pass
   ```

8. PRINSIP LISKOV SUBSTITUTION PRINCIPLE DILANGGAR
   Salah satu prinsip SOLID: "Child class harus bisa menggantikan Parent class 
   tanpa merusak program."
   
   Jika nama method beda:
   - Child class tidak bisa menggantikan Parent class
   - Kode yang menggunakan Parent akan error jika diberi Child
   - Prinsip OOP dilanggar


Analogi Dunia Nyata:
--------------------
Bayangkan remote TV yang punya tombol "Power":
- Semua TV (Sony, Samsung, LG, dll) HARUS merespons tombol "Power"
- Tidak boleh ada TV yang menggunakan tombol "Hidupkan" atau "Start"
- Jika nama tombol berbeda, remote universal tidak akan bekerja

Tombol "Power" = nama method yang harus sama (serang)
Berbagai merk TV = berbagai class (Mage, Archer, Fighter)
Cara TV menyala = implementasi berbeda (bola api, panah, pedang)


KESIMPULAN PERTANYAAN 2:
-------------------------
Jika nama method diubah dari serang() menjadi tembak_panah(), program akan 
error atau menjalankan method default dari parent class, bukan implementasi 
Archer yang unik.

Nama method HARUS PERSIS SAMA karena:
1. Polymorphism bergantung pada konsistensi nama
2. Loop/fungsi umum tidak bisa bekerja jika nama beda
3. Interface/kontrak dilanggar
4. Dynamic dispatch tidak berfungsi
5. Tidak ada cara otomatis mapping nama berbeda
6. Kode jadi rumit dan tidak scalable
7. Override tidak terjadi jika nama beda
8. Melanggar prinsip Liskov Substitution Principle

Konsistensi nama method adalah INTI dari Polymorphism. Tanpa konsistensi nama, 
Polymorphism tidak akan bekerja sama sekali.