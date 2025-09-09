Ahmad Aqeel Saniy - 2306275941
PBP A

Tautan PWS aplikasi: https://ahmad-aqeel-kickoffstandoff.pbp.cs.ui.ac.id/

Jawaban pertanyaan:


I. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step


    1. Membuat proyek Django baru.
        Untuk membuat proyek Django baru, pertama saya membuat direktori baru untuk proyek Django tersebut.
        Kemudian saya mengunduh dependencies setelah mengaktifkan virtual environment.
        Lalu di command prompt, saya membuat proyek baru dengan perintah `django-admin startproject kickoff_standoff .`
        Setelah itu, dibuatlah file .env dan .env.prod dengan konfigurasi yang ditentukan dari email Fasilkom UI.
        Selanjutnya, ditambahkan konfigurasi tertentu pada file settings.py untuk mencakup environment variables, allowed host, production, dan database.
        Akhirnya, saya mengunggah proyek Django ke repository GitHub dan ke PWS setelah menambahkan berkas .gitignore.

    2. Membuat aplikasi dengan nama main pada proyek tersebut.
        Untuk membuat aplikasi dengan nama main, saya mengaktifkan virtual environment di direktori proyek.
        Lalu dijalankan perintah `python manage.py startapp main` dalam command prompt di direktori proyek.
        Django akan otomatis membuat aplikasi main, sehingga saya hanya menambahkan aplikasi main ke dalam variabel INSTALLED_APPS dalam settings.py di direktori kickoff_standoff

    3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
        Pertama, dalam direktori proyek kickoff_standoff, saya membuka file urls.py dan mengimpor fungsi include dari django.urls.
        Kemudian, saya menambahkan rute URL yang mengarah ke tampilan aplikasi main di dalam list urlpatterns.

    4. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib.
        Saya membuka file models.py dalam aplikasi main, lalu mengimpor models dari django.db.
        Lalu dibuatlah class model dengan nama Product, yang memiliki setiap atribut wajib didalamnya.
        Saya juga menambahkan beberapa atribut opsional seperti stock, category, brand, dan rating.
        Akhirnya, jalankan perintah migrasi model dengan perintah `python manage.py makemigrations` kemudian `python manage.py migrate`

    5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
        Pada file views.py di dalam direktori main, saya mengimpor render dari django.shortcuts.
        Lalu saya menambahkan fungsi show_main, yang berisi context berisi nama aplikasi, NPM, nama penuh saya, dan juga kelas.
        Kemudian fungsi akan mereturn `render(request, "main.html", context)`.

    6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
        kita membuat file urls.py dalam direktori main, kemudian kita isi dengan kode
        ```from django.urls import path
        from main.views import show_main

        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
        ]
        ```

    7. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
        Untuk mendeploy aplikasi ke PWS, setelah mengakses situs PWS saya membuat proyek baru dengan nama yang sesuai untuk aplikasinya.
        Lalu pada di bagian environs, saya memasukkan nilai yang sama seperti isi file .env.prod.
        Setelah itu saya memasukkan url PWS ke dalam allowed host di settings.py.
        Akhirnya saya menjalankan perintah yang diberikan PWS di dalam command prompt, dan mengisi kredensial seperti yang telah diberikan PWS.


II. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

    https://drive.google.com/file/d/1QH59nVDzaspwLZs3LmOYU0LFxX08meJy/view?usp=sharing
    Dalam gambar, dapat dilihat bahwa pertama klien akan mengirim request ke aplikasi dari web browser. Kemudian aplikasi akan mengecek apakah request dilakukan ke url yang valid/ada dalam urls.py di proyek.
    Jika url tidak ada dalam proyek, maka aplikasi akan mengirimkan error 404 not found. Namun jika url ada, maka aplikasi akan routing kepada views yang memiliki url yang sesuai berdasarkan urls.py.
    User akan berinteraksi dengan views.py dalam aplikasi, views.py akan menangani logika operasi, melakukan respons, dan memproses data yang di request oleh user.
    Views.py ini akan ditampilkan sesuai dengan templates melalui file HTML. File HTML akan menentukan bagaimana visual aplikasi yang ditampilkan saat ini sehingga user mudah berinteraksi dengan views.py.
    Saat user berinteraksi, views.py akan menggunakan data yang tersimpan dalam database. Data-data tersebut strukturnya di definisikan oleh models.py sehingga bentuknya konsisten.
    Selain itu, cara views berinteraksi dengan database juga ditentukan oleh models.py agar tidak terjadi kerusakan dalam database.


III. Jelaskan peran settings.py dalam proyek Django!

    Peran settings.py adalah sebagai konfigurasi utama dalam keseluruhan proyek Django. settings.py mengatur konfigurasi aplikasi-aplikasi yang ada dalam proyek sehingga mereka dapat diakses.
    Selain itu, settings.py juga mengatur koneksi database dengan aplikasi sehingga aplikasi dapat mengakses database yang disimpan.
    settings.py menyangkut keamanan proyek, dengan membatasi di mana proyek dapat di hosting agar integrasi proyek aman dari ancaman luar.
    Terdapat beberapa peran lain yang settings.py lakukan, seperti konfigurasi user authentication, konfigurasi template, konfigurasi direktori file, dan konfigurasi bahasa dan waktu.


IV. Bagaimana cara kerja migrasi database di Django?

    Migrasi pada Django dilakukan setelah kita mengubah file models.py dalam proyek. Hal ini dikarenakan models.py menentukan database, sehingga kemungkinan skema database akan berubah dalam aplikasi tersebut.
    Pertama, akan dijalankan perintah `python manage.py makemigrations` agar Django membuat file migrasi.
    Pada tahap ini, Django akan otomatis melakukan migrasi pada aplikasi, lalu setelah dijalankan perintah `python manage.py migrate`, maka Django akan menerapkan migrasi yang dilakukan.


V. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

    Django dijadikan sebagai permulaan pembelajaran pengembangan perangkat lunak karena Django memiliki fitur-fitur yang cukup lengkap, sehingga pemula tidak perlu mengintegrasikan beberapa library yang diperlukan.
    Selain itu, struktur proyeknya tersusun dengan baik dan mudah dimengerti sehingga pemula dapat membuat aplikasi sederhana dengan cepat.
    Django juga memiliki cukup banyak dokumentasi, sehingga pemula dapat belajar dengan mudah. Tidak hanya itu, Django menggunakan bahasa pemrograman phyton yang termasuk sederhana dan mudah dipelajari.


VI. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

    Tidak, tutorial sudah sangat baik dan mudah dimengerti.