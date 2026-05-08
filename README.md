📘 Praktikum Object-Oriented Programming (OOP) Python
Repository ini berisi dokumentasi, latihan, dan analisis mendalam mengenai konsep Object-Oriented Programming menggunakan bahasa pemrograman Python. Materi mencakup enam pilar utama OOP: Class & Object, Inheritance, Encapsulation, Abstraction, dan Polymorphism.

🦸 Latihan 1: Membuat Class & Object
Fokus: Inisialisasi atribut dan manipulasi objek sederhana.

📝 Analisis
Pertanyaan: Apa yang terjadi jika kamu mengubah hero1.hp menjadi 500 setelah baris hero1 = Hero...? Coba lakukan print(hero1.hp).

Jawaban:
Nilai HP dari objek hero1 (Layla) akan berubah dari nilai awal 100 menjadi 500. Hal ini karena atribut hp pada latihan ini masih bersifat public, sehingga nilainya dapat diakses dan diubah langsung dari luar class. Output program akan menampilkan angka 500.

🤝 Latihan 2: Interaksi Antar Objek
Fokus: Komunikasi antar instance class melalui method.

📝 Analisis
Pertanyaan: Perhatikan parameter lawan pada method serang. Parameter tersebut menerima sebuah objek utuh, bukan hanya string nama. Mengapa ini penting?

Jawaban:
Mengirimkan objek utuh memberikan fleksibilitas dan fungsionalitas penuh:

Akses Atribut: Kita bisa mengakses semua atribut lawan (HP, Defense, Nama) secara langsung.

Manipulasi Langsung: Kita bisa langsung mengurangi nilai HP objek lawan di dalam method tersebut.

Integritas Data: Perubahan yang terjadi pada objek lawan akan tersimpan secara permanen pada instance tersebut, bukan sekadar mengubah variabel lokal.

🧬 Latihan 3: Pewarisan (Inheritance)
Fokus: Reusabilitas kode menggunakan Class Induk dan Class Anak.

📝 Analisis
Pertanyaan 1: Pada class Mage, jika baris super().__init__(name, hp, attack_power) dihapus atau dikomentari, apa yang terjadi?

Jawaban: Kode akan mengalami error saat dijalankan karena proses inisialisasi class induk terputus.

Pertanyaan 2: Error apa yang muncul saat memanggil eudora.info()? Mengapa hal itu terjadi padahal kita mengirim parameter "Eudora"?

Jawaban: Muncul AttributeError: 'Mage' object has no attribute 'name'.

Penyebab: Tanpa fungsi super().__init__, constructor milik class induk (Hero) tidak pernah dijalankan. Akibatnya, atribut name, hp, dan attack_power tidak pernah dibuat/disimpan ke dalam memori objek Mage, meskipun argumennya dikirim saat pembuatan objek.

🔐 Latihan 4: Enkapsulasi
Fokus: Keamanan data melalui Private Attributes dan Getter/Setter.

🧪 4.1 Percobaan Hacking
Akses Paksa: Nilai HP tetap muncul jika diakses melalui hero1._Hero__hp.

Konsep Name Mangling: Python tidak benar-benar menyembunyikan atribut private, melainkan mengubah namanya menjadi _NamaClass__namaAtribut. Kita tidak boleh melakukannya karena melanggar prinsip data hiding dan dapat menyebabkan inkonsistensi data jika dilakukan secara sembarangan.

🧪 4.2 Uji Validasi
Tanpa Validasi: Jika logic if/elif dihapus, HP bisa bernilai negatif (misal: -100). Ini merusak logika permainan (integritas data).

Pentingnya Setter: Method Setter bertindak sebagai "Penjaga Gerbang". Ini mencegah cheating, memastikan data tetap logis (HP tidak mungkin negatif), dan mencegah crash pada sistem lain yang mengandalkan keakuratan data tersebut.

🧾 Latihan 5: Abstraction dan Interface
Fokus: Membuat kontrak antar class menggunakan ABC (Abstract Base Class).

📝 Analisis
Pertanyaan: Apa yang terjadi jika method serang pada class Hero dihapus?

Error: TypeError: Can't instantiate abstract class Hero with abstract method serang.

Arti Error: Python melarang pembuatan objek dari class yang masih memiliki "janji" (method abstrak) yang belum ditepati.

Konsekuensi: Jika kita lupa mengimplementasikan method yang dijanjikan di Interface, program tidak akan bisa berjalan. Ini memastikan setiap karakter baru (Mage, Fighter, dll) wajib memiliki fungsi serangan yang spesifik.

🔄 Latihan 6: Polymorphism
Fokus: Satu interface, banyak implementasi.

📝 Analisis
Skenario: Menambahkan class Healer ke dalam list pasukan tanpa mengubah loop for.

Hasil: Program berjalan sangat lancar.

Keuntungan bagi Programmer:

Skalabilitas: Kita bisa menambah ribuan jenis hero baru tanpa perlu mengubah kode logika utama game.

Efisiensi: Cukup memanggil method yang sama (serang()), dan setiap objek akan merespons sesuai dengan identitas class-nya masing-masing.

📚 Penutup
Melalui praktikum ini, dapat disimpulkan bahwa penerapan OOP membuat:

Struktur Kode: Lebih rapi dan terorganisir.

Keamanan: Data lebih terlindungi dari akses ilegal.

Fleksibilitas: Program sangat mudah untuk dikembangkan dalam skala besar (Scalable).

Dibuat untuk memenuhi tugas Praktikum Pemrograman Berorientasi Objek.
