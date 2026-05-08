📘 Praktikum OOP Python
Repository ini berisi latihan dan analisis Object Oriented Programming menggunakan Python. Materi mencakup Class, Object, Inheritance, Encapsulation, Abstraction, dan Polymorphism.

🦸 Latihan 1. Membuat Class Hero
Latihan1

PERTANYAAN:
Apa yang terjadi jika kamu mengubah hero1.hp menjadi 500 setelah baris hero1 = Hero...? Coba lakukan print(hero1.hp).

JAWABAN:
Yang terjadi jika mengubah hero1.hp menjadi 500 setelah baris hero1 = Hero adalah nilai HP dari objek hero1 (Layla) akan berubah dari nilai awal 100 menjadi 500. Ketika kita menjalankan print(hero1.hp), program akan menampilkan angka 500.

🤝 Latihan 2. Interaksi Antar Objek
Latihan2

PERTANYAAN:
Perhatikan parameter lawan pada method serang. Parameter tersebut menerima sebuah objek utuh, bukan hanya string nama. Mengapa ini penting?

JAWABAN:
Parameter lawan pada method serang menerima sebuah objek utuh (bukan hanya string nama) karena hal ini sangat penting dalam pemrograman berorientasi objek. Berikut adalah alasan-alasan pentingnya:

🧬 Latihan 3. Pewarisan Inheritance
Latihan3

PERTANYAAN 1:
Pada class Mage, coba hapus (atau jadikan komentar #) baris kode super().init(name, hp, attack_power). Kemudian jalankan programnya. Apa yang terjadi?

JAWABAN: Kode mengalami error setelah dijalankan.

PERTANYAAN 2:
Error apa yang muncul saat kamu mencoba melihat info Eudora (eudora.info())? Mengapa error tersebut mengatakan Mage object has no attribute 'name', padahal kita sudah mengirim nama "Eudora" saat pembuatan objek?

JAWABAN: Error yang muncul saat memanggil eudora.info() adalah AttributeError: 'Mage' object has no attribute 'name'.

Error ini terjadi karena pada class Mage, constructor milik class Induk (Hero) tidak dipanggil, sehingga atribut name, hp, dan attack_power tidak pernah dibuat di dalam objek Mage, meskipun nilai-nilai tersebut dikirim saat pembuatan objek.

🔐 Latihan 4. Enkapsulasi
Latihan4

TUGAS ANALISIS 4.1: PERCOBAAN HACKING
Pertanyaan 1: Apakah nilai HP muncul atau Error ketika mengakses hero1._Hero__hp?

Jawaban: Nilai HP tetap muncul dan tidak error. Ketika saya menambahkan baris kode print(f"Mencoba akses paksa: {hero1._Hero__hp}"), program berhasil menampilkan nilai HP yang tersimpan dalam atribut private __hp.

Pertanyaan 2: Mengapa Python masih mengizinkan akses ini (konsep Name Mangling) dan mengapa kita tetap tidak boleh melakukannya dalam standar pemrograman yang baik?

Jawaban: Python masih mengizinkan akses ini karena Python menggunakan konsep yang disebut "Name Mangling". Ketika kita membuat atribut private dengan tanda __ (double underscore), Python tidak benar-benar menyembunyikan atribut tersebut, melainkan mengubah namanya secara internal menjadi _NamaClass__namaAtribut. Dalam kasus ini, __hp diubah menjadi _Hero__hp.

TUGAS ANALISIS 4.2: UJI VALIDASI
Pertanyaan 1: Apa yang terjadi pada data HP Hero ketika logic validasi (if dan elif) dihapus dari method set_hp, kemudian melakukan hero1.set_hp(-100)?

Jawaban: Ketika logic validasi dihapus dari method set_hp sehingga isinya hanya berisi self.__hp = nilai_baru, maka HP Hero akan langsung diset menjadi -100 tanpa ada pemeriksaan atau pencegahan. Ini sangat berbahaya karena dalam konteks game, HP (Health Point) yang bernilai negatif tidak masuk akal dan melanggar aturan game.

Dampak yang terjadi:

Data menjadi tidak valid: Hero memiliki HP -100, yang secara logika tidak mungkin (HP minimal seharusnya 0).

Bug dalam game: Kondisi ini bisa menyebabkan error atau perilaku aneh dalam game. Misalnya, ketika mengecek apakah hero sudah mati (biasanya dengan kondisi if hp <= 0), hero dengan HP negatif mungkin masih dianggap hidup tergantung bagaimana kondisinya ditulis.

Exploitasi: Pemain atau hacker bisa memanipulasi HP menjadi nilai yang tidak wajar untuk mendapatkan keuntungan tidak adil (cheating).

Inkonsistensi data: Jika ada bagian lain dari program yang mengasumsikan HP selalu bernilai 0 atau positif, program bisa crash atau menghasilkan hasil yang salah.

Pertanyaan 2: Jelaskan mengapa keberadaan method Setter sangat penting untuk menjaga integritas data dalam game!

Jawaban: Method Setter sangat penting untuk menjaga integritas data dalam game karena beberapa alasan krusial. Method Setter adalah "penjaga gerbang" yang memastikan hanya data yang valid dan aman yang bisa masuk ke dalam atribut object. Dalam game development, ini adalah praktik wajib untuk mencegah bug, cheating, dan memastikan game berjalan sesuai dengan aturan yang telah ditetapkan. Tanpa setter dengan validasi yang baik, integritas data game akan mudah rusak dan pengalaman bermain akan terganggu.

🧾 Latihan 5. Abstraction dan Interface
Latihan5

PERTANYAAN 1: MELANGGAR KONTRAK
Pada class Hero, hapus (atau jadikan komentar #) seluruh blok method def serang(self, target):. Jalankan programnya.

a) Error apa yang muncul? b) Jelaskan dengan bahasamu sendiri, apa arti pesan error "Can't instantiate abstract class Hero with abstract method..."? c) Apa konsekuensinya jika kita lupa membuat method yang sudah dijanjikan di Interface?

JAWABAN:
a) Error yang Muncul:
Error yang muncul adalah:

TypeError: Can't instantiate abstract class Hero with abstract method serang

atau bisa juga:

TypeError: Can't instantiate abstract class Hero with abstract methods: serang

🔄 Latihan 6. Polymorphism
Latihan6

PERTANYAAN 1: UJI SKALABILITAS (KEMUDAHAN MENAMBAH FITUR)
Tanpa mengubah satu huruf pun pada kode Looping (for pahlawan in pasukan:), buatlah satu class baru bernama Healer(Hero).

Isi method serang milik Healer dengan: print(f"{self.nama} tidak menyerang, tapi menyembuhkan teman!")

Masukkan objek Healer ke dalam list pasukan.

a) Pertanyaan: Apakah program berjalan lancar? b) Kesimpulannya, apa keuntungan Polimorfisme bagi seorang programmer ketika harus mengupdate game dengan karakter baru di masa depan?

JAWABAN:
a) Apakah Program Berjalan Lancar?
Ya, program berjalan dengan SANGAT LANCAR tanpa error sama sekali!

📚 Penutup

Latihan ini menunjukkan manfaat OOP. Kode lebih rapi. Data lebih aman. Program mudah dikembangkan. Cocok untuk game dan aplikasi skala besar.
