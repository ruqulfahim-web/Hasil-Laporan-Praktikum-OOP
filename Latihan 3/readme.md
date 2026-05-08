================================================================================
TUGAS ANALISIS 3: PEWARISAN (INHERITANCE)
Eksperimen Fungsi super()
================================================================================


PERTANYAAN 1:
================================================================================
Pada class Mage, coba hapus (atau jadikan komentar #) baris kode 
super().__init__(name, hp, attack_power). Kemudian jalankan programnya.
Apa yang terjadi?

JAWABAN:
Kode mengalami error setelah dijalankan.


PERTANYAAN 2:
================================================================================
Error apa yang muncul saat kamu mencoba melihat info Eudora (eudora.info())? 
Mengapa error tersebut mengatakan Mage object has no attribute 'name', padahal 
kita sudah mengirim nama "Eudora" saat pembuatan objek?

JAWABAN:
Error yang muncul saat memanggil eudora.info() adalah AttributeError: 'Mage' 
object has no attribute 'name'. 

Error ini terjadi karena pada class Mage, constructor milik class Induk (Hero) 
tidak dipanggil, sehingga atribut name, hp, dan attack_power tidak pernah 
dibuat di dalam objek Mage, meskipun nilai-nilai tersebut dikirim saat 
pembuatan objek.

Penjelasan Detail:
Ketika kita membuat objek Mage dengan eudora = Mage("Eudora", 80, 30, 100), 
Python hanya menjalankan constructor __init__ milik class Mage. Jika di dalam 
constructor Mage tidak ada pemanggilan super().__init__(), maka constructor 
class Hero tidak akan dijalankan sama sekali. Akibatnya, atribut name, hp, dan 
attack_power yang seharusnya dibuat oleh constructor Hero tidak pernah 
terinisialisasi. Yang terjadi hanya atribut mana yang dibuat, tetapi atribut 
dari parent class tidak ada.

Saat method info() dipanggil dan mencoba mengakses self.name, Python tidak 
menemukan atribut tersebut karena memang tidak pernah dibuat, sehingga muncul 
error AttributeError.


PERTANYAAN 3:
================================================================================
Jelaskan peran fungsi super() dalam menghubungkan data dari class Anak ke 
class Induk!

JAWABAN:
Fungsi super() berperan untuk memanggil constructor atau method milik class 
Induk agar class Anak dapat mewarisi dan menggunakan atribut serta perilaku 
yang didefinisikan di class Induk, sehingga data seperti name, hp, dan 
attack_power dapat terhubung dan digunakan oleh objek dari class Anak.

Penjelasan Detail:
Fungsi super() bertindak sebagai "jembatan" yang menghubungkan class Anak 
(Child) dengan class Induk (Parent). Ketika kita menulis super().__init__() 
di dalam constructor class Anak, Python akan:

1. Mencari class Induk (parent class) dari class yang sedang aktif
2. Memanggil method __init__ milik class Induk tersebut
3. Menjalankan semua inisialisasi yang ada di constructor class Induk
4. Membuat semua atribut yang didefinisikan di class Induk

Dengan demikian, objek dari class Anak akan memiliki semua atribut dari class 
Induk ditambah dengan atribut khusus miliknya sendiri. Dalam kasus Mage:
- Atribut dari Hero (melalui super): name, hp, attack_power
- Atribut khusus Mage: mana

Tanpa super(), class Anak hanya akan memiliki atribut miliknya sendiri dan 
tidak mewarisi atribut dari class Induk, sehingga konsep inheritance menjadi 
tidak berguna.