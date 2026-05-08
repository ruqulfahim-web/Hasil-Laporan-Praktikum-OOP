===============================================================================
TUGAS ANALISIS 1: MEMBUAT CLASS HERO
Memahami Atribut dan Modifikasi Nilai
================================================================================


PERTANYAAN:
================================================================================
Apa yang terjadi jika kamu mengubah hero1.hp menjadi 500 setelah baris 
hero1 = Hero...? Coba lakukan print(hero1.hp).


JAWABAN:
================================================================================
Yang terjadi jika mengubah hero1.hp menjadi 500 setelah baris hero1 = Hero 
adalah nilai HP dari objek hero1 (Layla) akan berubah dari nilai awal 100 
menjadi 500. Ketika kita menjalankan print(hero1.hp), program akan menampilkan 
angka 500.


PENJELASAN DETAIL:
================================================================================

Proses yang Terjadi:
--------------------
1. Saat objek dibuat dengan hero1 = Hero("Layla", 100, 15), atribut hp 
   diinisialisasi dengan nilai 100 di dalam constructor __init__.

2. Setelah objek terbuat, kita bisa mengakses dan mengubah atribut hp secara 
   langsung dengan menulis hero1.hp = 500.

3. Python akan mengganti nilai lama (100) dengan nilai baru (500) pada atribut 
   hp milik objek hero1.

4. Ketika print(hero1.hp) dijalankan, Python menampilkan nilai terbaru yaitu 500.


Contoh Kode dan Output:
-----------------------
```python
# Membuat objek hero1
hero1 = Hero("Layla", 100, 15)

# HP awal
print(hero1.hp)  # Output: 100

# Mengubah HP secara langsung
hero1.hp = 500

# HP setelah diubah
print(hero1.hp)  # Output: 500

# Menampilkan info lengkap
hero1.info()  # Output: Hero: Layla | HP: 500 | Power: 15
```


Kesimpulan:
-----------
Atribut objek dalam Python bersifat mutable (dapat diubah) dan dapat diakses 
serta dimodifikasi secara langsung dari luar class. Dalam contoh ini:
- Hero Layla yang awalnya memiliki HP 100
- Setelah diubah dengan hero1.hp = 500
- HP Layla menjadi 500

Namun perlu diingat, cara mengubah atribut secara langsung seperti ini (tanpa 
method setter) tidak disarankan dalam praktik OOP yang baik karena:
1. Tidak ada validasi (bisa diisi nilai yang tidak valid seperti HP negatif)
2. Melanggar prinsip encapsulation
3. Sulit untuk di-maintain di masa depan