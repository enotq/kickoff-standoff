Ahmad Aqeel Saniy - 2306275941
PBP A

Tautan PWS aplikasi: https://ahmad-aqeel-kickoffstandoff.pbp.cs.ui.ac.id/

<details>
<summary> Tugas Individu 2</summary>

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

</details>

<details>
<summary>Tugas Individu 3</summary>

Jawaban Pertanyaan:


I. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

    Data Delivery memiliki peran penting dalam pengimplementasian platform karena data delivery berperan dalam mengirimkan data dari database server ke bagian yang diperlukan ataupun sebaliknya, seperti misalnya:
    - Ke dalam aplikasi pengguna sehingga aplikasi dapat menampilkan informasi dari database melalui User Interface.
    - Mendapatkan pengguna mengirimkan informasi ke dalam database melalui User Interface aplikasi sehingga user lebih mudah berinteraksi dengan aplikasi.
    - Mengirimkan data ke sistem external, misalkan sistem diperlukan berkomunikasi dengan sistem external untuk menjalankan suatu proses (contohnya seperti pembayaran, sistem dapat berkomunikasi dengan bank).
    - Untuk ketersediaan data, artinya agar aplikasi dapat memiliki data yang konsisten dalam beberapa server sehingga tidak ada data yang hilang.
    - Untuk menjaga keamanan, data delivery dapat hanya mengirimkan data yang user bisa lihat melalui akun mereka sendiri sehingga isi database tidak bocor.
    Dan masih terdapat contoh lain yang lebih spesifik, namun hal-hal diatas merupakan contoh dasarnya.


II. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

    Secara umum, JSON lebih baik digunakan. Alasan utamanya adalah dibandingkan XML, JSON lebih mudah dibaca oleh manusia karena sintaksnya lebih rapih.
    Selain itu, karena sintaks JSON lebih simplistik, maka JSON juga dapat berukuran lebih kecil daripada XML dalam webpage yang berukuran besar.
    Tidak hanya itu, dalam parsing, JSON bersifat lebih cepat karena XML memerlukan parser khusus.

    Alasan diatas merupakan alasan utama mengapa JSON lebih populer dibandingkan XML, karena JSON lebih ringkas dan mudah dibaca, tidak hanya JSON diproses lebih cepat, tapi juga developer dapat dengan mudah menganalisis isi kontennya untuk misal bug fixing.


III. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

    Fungsi utama dari method is_valid() adalah sebagai validasi data input. Sebagai dasar, is_valid() akan melakukan field validation, Django akan mengecek form input dan memastikan tipe data yang dimasukkan sesuai.
    Tidak hanya itu, Django juga akan membersihkan data yang dimasukkan, artinya user tidak dapat memasukkan input yang memungkinkan bersifat berbahaya (contohnya seperti SQL injection).
    Validasi yang dilakukan is_valid() juga bersifat customizeable, sehingga developer dapat mengganti validasi yang dilakukan secara otomatis, dan menambahkan error handling sendiri.
    Maka, method is_valid() diperlukan untuk validation input data sehingga input data konsisten, serta sebagai layer keamanan.


IV. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

    Secara dasar, csrf_token diperlukan sebagai perlindungan dari cross site request forgery. Django menggunakan csrf_token untuk memvalidasi request POST yang dikirim, sehingga misalnya situs lain tidak dapat memalsukan identitas user.
    Selain itu, csrf_token juga memverifikasi input apakah input dilakukan oleh user atau bukan, ini dilakukan untuk mencegah automated attacks.
    Tanpa csrf_token, Django akan secara default menolak request yang dilakukan pengguna karena request POST tidak memiliki csrf_token yang valid.

    Penyerang dapat memanfaatkan csrf_token vulnerability dengan beberapa cara, misalnya dengan phishing site dimana saat user memasuki suatu situs berbahaya, penyerang dapat mengirimkan request POST melalui cookies untuk mendapatkan informasi sensitif seperti kredensial bank.
    Terdapat juga cara penyerangan dimana penyerang melakukan auto-submit pada sebuah form sehingga identitas user mudah diambil oleh penyerang.
    Selain itu, ada juga serangan melalui gambar, dimana penyerang menggunakan image tag untuk menjalankan request POST.


V. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).


    1. Menambahkan 4 fungsi views baru dalam format XML, JSON, XML by ID, dan JSON by ID
        Pertama, ditambahkan import baru dengan mengimport serializers dan HttpResponse
        Kemudian buat function show_xml dan show_json. Kedua function ini memiliki format yang sama dengan sedikit perbedaan. Di dalamnya, dibuat variabel untuk menyimpan query seluruh data untuk objek Product.
        Buatlah variabel untuk menyimpan hasil serialisasi data query menjadi bentuk data masing-masing ("xml" untuk show_xml dan "json" untuk show_json).
        Akhirnya buatlah return function dalam bentuk HttpResponse dengan parameter variabel serialisasi tersebut dan parameter content_type sesuai dengan function masing-masing.

        Untuk function XML by ID dan JSON by ID, bentuk functionnya juga sangat serupa, dengan perbedaan pada variabel penyimpanan query data, ditambahkan filter dengan primary key berdasarkan id sehingga tidak diambil keseluruhan data.

    2. Membuat routing URL untuk masing-masing views yang telah ditambahkan
        Routing URL dilakukan dengan cara yang sama, pertama akan diimport dalam main/urls.py function yang telah dibuat dari main.views.
        Kemudian dalam urlpatterns, hanya ditambahkan path masing-masing dengan function yang telah dibuat agar function dapat diakses melalui path tersebut.

    3. Membuat halaman yang menampilkan data objek model yang memiliki tombol "add" yang akan redirect ke halaman form, serta tombol "detail" pada setiap data objek model yang ditampilkan
        Untuk halaman penampilan data objek, saya menggunakan bentuk card dengan setiap objek memiliki nama, harga, kategori, dan rating. Setelah menyetel css style untuk objek halaman tersebut, ditambahkan for loop yang akan iterasi semua objek product dalam database.
        Dalam setiap iterasi, objek akan ditampilkan dalam bentuk card dengan data yang ditampilkan merupakan data yang diambil dari setiap objek dengan format `{{ product.[atribut] }}`.
        Ditambahkan juga function tambahan, dimana jika produk tidak memiliki gambar/thumbnail, maka hanya akan ditampilkan nama produk. Terdapat juga tag featured yang hanya akan muncul jika produk bersifat featured.
        Selain itu, untuk harga saya tampilkan berdasarkan stock, jika stock telah habis maka harga akan digantikan string "Out of stock!".

        Diatas card-card tersebut, saya membuat tombol "Add product" yang berisi link redirect user ke halaman form penambahan product. Tombol menggunakan css styling yang sudah saya tentukan pada awal html.

        Kemudian untuk tombol "detail", saya mengimplementasikannya dengan cara berbeda. Setiap card objek produk yang ditampilkan merupakan button juga, yang dapat ditekan oleh user agar dapat di redirect ke halaman detail produk.
        Hal ini saya implementasikan dengan objek card memiliki link ke detail produk masing-masing dan menambahkan atribut agar keseluruhan card dapat ditekan layaknya sebuah button.

    4. Membuat halaman form untuk menambahkan objek model pada app sebelumnya
        Halaman form menggunakan method `{{ form.as_table }}` yaitu method built-in dalam Django yang akan membuat form secara otomatis.
        Oleh karena itu tidak perlu banyak ditambahkan dalam html kecuali jika penampilannya ingin diganti. Pengisian pada halaman form penambahan product akan sesuai dengan atribut-atribut yang diperlukan objek product.
        Dibawah function tersebut, hanya tinggal diatambahkan button submit, dimana Django akan secara otomatis menambahkannya ke database objek Product.

    5. Membuat halaman yang menampilkan detail dari setiap data objek model
        Halaman detail pertama memiliki sebuah button yang akan redirect user kembali ke halaman utama. Kemudian satu-satu saya menambahkan atribut yang perlu ditampilkan.
        Setiap baris ditambahkan format `{{ product.[atribut] }}` sehingga halaman dapat menampilkan detail produk tersebut. Beberapa atribut saya tambahkan ketentuan tertentu.
        Misalnya detail produk menampilkan jika produk berupa featured product jika product.is_featured adalah true. Selain itu, harga produk akan digantikan dengan "Out of stock!" jika stok produk telah habis.

</details>

<details>
<summary>Tugas Individu 4</summary>

Jawaban pertanyaan:


I. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

    AuthenticationForm merupakan form yang sudah disediakan Django untuk menangani proses login dan authentication user. Berbeda dengan form reguler yang menangani objek, form ini akan memvalidasi kredensial yaitu username dan password.
    Kelebihan AuthenticationForm adalah sudah datang dengan fitur keamanan seperti password hashing, brute force protection, dan account lockout. Selain itu, AuthenticationForm juga memiliki function user status validation yang dapat mengecek apakah akun aktif dan tidak di-disable.
    AuthenticationForm juga memiliki integrasi dengan Django Auth System, sehingga hal seperti user model, session management, dan user permission sudah di handle secara otomatis oleh Django.
    Semua hal tersebut juga bersifat customizable, sehingga jika developer ingin mengganti format sesuatu, misalnya membuat custom user sendiri, maka AuthenticationForm tetap bisa bekerja.

    Kekurangan AuthenticationForm secara faktor merupakan karena form ini bentuknya basic, sehingga untuk authentication dengan cara lebih kompleks seperti misalnya login melalui email, nomor telepon, atau social media, serta two-factor authentication, AuthenticationForm perlu dimodifikasi dengan override yang cukup banyak.
    Selain itu, untuk beberapa modern frontend, karena AuthenticationForm mengembalikan HTML form, maka diperlukan custom implementation untuk mereturn response lain seperti JSON.

    Maka dapat disimpulkan, AuthenticationForm sudah cukup baik untuk menghandle simple authentication tanpa langkah kompleks, namun untuk sistem user yang lebih kompleks, kemungkinan harus dibuat custom AuthenticationForm untuk menghandle langkah-langkah tersebut.


II. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

    Autentikasi merupakan proses verifikasi user, lebih jelasnya adalah proses memastikan bahwa akun yang diakses memang benar-benar milik user. Hal ini dilakukan melalui password, OTP code, verification through email.
    Otorisasi merupakan proses menentukan user permission, lebih jelasnya adalah menentukan aksi dan akses yang dapat user itu lakukan, seperti user dapat edit profile sendiri, namun tidak punya orang lain.

    Django mengimplementasikan autentikasi melalui user model dengan username dan password, user model dapat ditambahkan atribut custom seperti misalnya email. Lalu Django juga memanage session secara otomatis untuk user, serta dapat memiliki middleware untuk autentikasi otomatis.
    Django juga menyediakan login dan logout yang dapat dengan mudah digunakan untuk membantu developer membuat proses autentikasi dasar, proses tersebut akan secara otomatis melakukan password hashing untuk user untuk menjaga keamanan juga.

    Django mengimplementasikan otorisasi melalui permission system dalam setiap user, permission system juga dapat diberikan diberikan kepada sekelompok orang dengan role-based access.
    Function dalam Django views juga dapat diberikan decorators seperti `@login_required)` untuk memastikan tidak semua user dapat mengakses sesuatu konten. Django juga mensupport template tags yang akan menampilkan layar tertentu dalam halaman yang sama melalui HTML.


III. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

    Session menyimpan data ke server mengenai user client. Kelebihan penggunaan session adalah keamanan, karena session disimpan langsung dalam server, ini lebih relatif aman daripada disimpan pada client user.
    Selain itu, karena penyimpanannya di server, maka secara dasar juga memiliki storage yang lebih besar, sehingga dapat menyimpan lebih banyak data. Tidak hanya itu, session dapat disimpan dalam backends tertentu, dengan proteksi melalui csrf_token dan cleanup otomatis.

    Namun, karena session harus menyimpan semua session data, maka dapat memakan banyak server resources saat aplikasi memiliki banyak jumlah user.
    Oleh karena itu, diperlukan juga cleaning dalam sebuah server untuk menghilangkan session yang sudah tidak terpakai agar storage server tidak penuh.
    Ada juga permasalahan yaitu session bergantung dengan cookies untuk mendapat session ID, sehingga jika user mematikan cookies, session tidak dapat diakses.

    Sedangkan, cookies menyimpan data-data kecil ke dalam browser client user. Kelebihan cookies adalah karena data disimpan pada browser client, data tidak memakan banyak storage pada server database.
    Cookies juga dapat digunakan dalam jangka lama (seperti remember me option), dan dapat digunakan dalam beberapa domain berbeda (seperti misal website UI).

    Terdapat juga kekurangan cookies, seperti karena cookies menyimpan data kecil, cookies memiliki size limitation, sehingga tidak menyimpan data yang terlalu banyak.
    Cookies juga lebih rentan dalam keamanan, penyerang dapat mengambil cookies atau menginject sesuatu melalui cookies untuk mendapatkan informasi sensitif.
    Seperti disebutkan pada bagian session, cookies dapat dimatikan oleh user sehingga tidak dapat digunakan oleh aplikasi.


III. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

    Cookies secara default tidak aman untuk digunakan, terdapat banyak risiko potensial yang harus diwaspadai seperti XSS attack (mencuri cookies),
    CSRF attacks, user manipulation, dapat di intercept di HTTP connections, dan memiliki ukuran yang terbatas.

    Django menangani masalah berikut dengan menggunakan HttpOnly flag untuk XSS attacks, menggunakan Secure flag untuk HTTPS enforcement, menggunakan SameSite attribute dan csrf_token untuk menangani CSRF attacks serta memiliki middleware untuk CSRF,
    membuat session key, dan memvalidasi cookies secara otomatis.


IV. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).


    1. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya.
        Pertama, akan diimpor `UserCreation Form, messages, AuthenticationForm, authenticate, login, logout` ke dalam views.py.
        Untuk membuat fungsi registrasi, kita menggunakan UserCreationForm built in milik Django dengan memasukkannya kedalam suatu variabel form.
        Setelah membuat conditional untuk request POST, kita memanggil UserCreationForm dan memanggil function `is_valid()` untuk mengecek input form.
        Lalu, jika true, maka buatlah agar registration disimpan dengan `save()` lalu redirect user ke halaman login. Seperti halaman views lain, kita perlu membuat return render.

        Untuk membuat fungsi login, kita gunakan AuthenticationForm built in milik Django, dan memasukkannya kedalam suatu variabel, dengan parameter data dari request POST.
        Setelah membuat conditional untuk mengecek apakah input valid, carilah user dari database dengan `user = form.get_user()` dan panggil function login dengan parameter request dan user.
        Lalu, redirect user ke halaman utama, dan return render seperti views lainnya.

        Untuk membuat fungsi logout, kita hanya perlu memanggil function logout dengan parameter request, lalu return redirect ke halaman login.

        Agar ketiga fungsi tersebut dapat dijalankan, kita akan mengimpor ketiga fungsi kedalam main/urls.py, kemudian memasukkan path url masing-masing kedalam urlpatterns.
        Perlu ditambahkan juga tombol untuk logout pada halaman utama, yang akan redirect ke url logout.

    2. Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.
        Pembuatan akun pengguna cukuplah mudah, kita dapat menjalankan aplikasi secara lokal dengan `python manage.py runserver` pada direktori proyek. Kemudian kita hanya gunakan metode register yang sudah kita buat.
        Untuk pembuatan data, kita pertama perlu log in dengan akun pengguna tersebut, kemudian dengan menekan tombol "Add Product" kita dapat langsung mengisi form penambahan produk seperti yang diperlukan.

    3. Menghubungkan model Product dengan User.
        Untuk menghubungkan model Product dengan User, pertama kita harus mengimport User pada main/models.py, dan menambahkan variabel user pada class Product.
        Variabel tersebut berupa atribut berisi ForeignKey(User), dengan CASCADE on delete sehingga jika user dihapus, maka produk juga terhapus. Kita juga harus menambahkan null=True pada parameter sehingga produk yang sebelumnya ada tetap valid tanpa user.
        Kemudian, pada views.py, kita tambahkan decorator `@login_required` pada fungsi add_product. Kemudian setelah pengecekan `is_valid()`, kita akan menambahkan variabel entry untuk produk, yang didapat dari input form.
        Kemudian kita masukkan user yang mengisi form tersebut dengan `product_entry.user = request.user`, sebelum menyimpan isi input dan meredirect kembali ke halaman utama.

    4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.
        Untuk menambahkan detail informasi tersebut, pertama kita harus mengimport datetime, HttpResponseRedirect, dan reverse ke dalam main/views.py.
        Kemudian pada bagian fungsi login_user, kita membuat variabel reverse yang berupa `HttpResponseRedirect(reverse("main:show_main"))`, kemudian kita akan set cookie response tersebut
        menggunakan parameter last login dan waktu last_login. Kita akan mengambil waktu last_login menggunakan datetime.datetime.now() yang diubah menjadi string. Kemudian pada context di show_main,
        kita hanya tambahkan 'last_login' sebagai request.COOKIES.get('last_login', 'Never') ke context. Kita juga tambahkan 'username' sebagai request.user.username yang akan mengambil username user sekarang.
        Akhirnya, kita hanya tambahkan bagian yang menunjukkan sesi terakhir login serta username user yang sedang login pada halaman utama.

</detail>

<details>
<summary>Tugas Individu 5</summary>

Jawaban Pertanyaan:


I. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

    Urutan prioritas pengambilan CSS selector dari tertinggi ke terendah diambil dari skala prioritas dibawah:

    1. Origin and Importance
        Origin artinya asal CSS itu ada, terdapat 3 skala prioritas di dalamnya. Pertama adalah Author dengan prioritas tertinggi. Artinya CSS tersebut berasal dari developer itu sendiri (sudah dibuat dari awal), sehingga akan mengganti seluruh CSS style lainnya.
        Kedua adalah user, yaitu jika user dapat mengganti atribut CSS pada client user, seperti mengganti font, ukuran, dan warna. Yang terakhir adalah User Agent, yaitu dimana browser memiliki default style sendiri, contohnya seperti jika bowser memiliki dark-mode support, aplikasi dapat juga memiliki mode gelap secara otomatis.

        Importance artinya CSS tersebut memiliki syntax `!important`. Syntax ini diletakkan pada suatu CSS style yang membuatnya memiliki prioritas tertinggi, artinya elemen yang terkait akan pasti mengikuti CSS tersebut.

    2. Selector Specifity
        Selector specifity artinya lokasi, atau syntax yang css gunakan, dengan dibagi kembali menjadi beberapa urutan prioritas.

        Pertama adalah inline styles, artinya CSS terdapat langsung didalam atribut `styles` pada suatu elemen. Elemen pasti akan mengikuti style ini.

        Kedua adalah ID Selectors, artinya CSS menentukan style sebuah elemen melalui ID. Style yang ditentukan dimasukkan atribut kelompok elemen dengan ID tertentu, ditandai dengan `#` diikuti nama ID seperti `#header`. Elemen dengan ID tersebut akan mengikuti style yang ditentukan.

        Ketiga adalah Class Selectors, artinya CSS menentukan style sebuah elemen dengan class tersebut. Style yang ditentukan dimasukkan atribut dengan class tertentu, ditandai dengan `.` diikuti nama class seperti `.button`.

        Keempat adalah Element Selectors, artinya CSS menentukan style seluruh elemen yang ditentukan tersebut. Style yang ditentukan dimasukkan atribut elemen tertentu, ditandai dengan nama elemen seperti `div`.

    3. Source Order
        Jika terdapat beberapa stylesheets yang dimasukkan kedalam bagian `<head>` sebuah HTML, maka HTML akan mengikuti stylesheets yang paling akhir dan mengganti styling stylesheets awal jika mengikat atribut yang sama.

    4. Initial and Inherited Property
        Sebuah elemen HTML dapat memiliki CSS styling yang ditandai dengan `intitial` dan/atau `inherit`. `inherit` property akan membuat elemen tersebut menggunakan nilai style yang dimiliki parentnya, jika parent mengganti style maka elemen juga akan ikut mengganti style. Sedangkan `initial` akan mengembalikan nilai default browser yang ditentukan browser itu sendiri.


II. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!

    Responsive design memiliki beberapa alasan yang membuatnya penting dalam pengembangan aplikasi web, contohnya ialah membuatnya dapat bekerja dengan benar pada perangkat yang berbeda (multi-device usage) seperti desktop, smartphone, dan tablet.
    Selain itu, dengan responsive design maka user experience juga akan meningkat, karena terdapat support untuk beberapa perangkat berbeda sehingga user dapat lebih nyaman menggunakan aplikasi di semua perangkat.
    Konsep ini juga dapat meningkatkan cost efficiency, karena kita tidak akan perlu membuat beberapa kode berbeda untuk semua perangkat, dengan hanya satu codebase, aplikasi dapat bekerja dengan benar pada seluruh perangkat.

    Contoh aplikasi yang sudah responsive adalah Facebook. Facebook memiliki responsive design yang akan mengubah layout dan UI berdasarkan dengan ukuran layar. Selain itu bentuk halaman juga berubah jika kita menggunakan perangkat berbeda, seperti beberapa tombol menu dimasukkan kedalam satu tombol yang dapat memuat opsi menu lain pada smartphone, sehingga mudah memilih opsi dan tidak mengganggu penampilan pada layar kecil.

    Contoh aplikasi yang belum responsive adalah SIAKNG. SIAKNG belum memiliki responsive design karena layout dan UI tetap sama pada beberapa ukuran layar maupun perangkat yang berbeda. Dapat dilihat dengan mudah bahwa jika kita membuka aplikasi pada smartphone, tombol menu dan elemen lainnya masih sama persis seperti pada di desktop, sehingga sulit untuk memilih menu tertentu (contohnya seperti mau melihat IRS maka kita harus zoom in pada aplikasi agar mudah memencet opsi tersebut).


III. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

    Jika dilihat seperti model kotak, content akan terletak di dalam padding, padding terletak di dalam border, dan border terletak di dalam margin.

    Padding merupakan area diantara content dan border, fungsinya adalah untuk memberikan ruang pada elemen. Ruang ini akan terpengaruh dengan elemen tersebut, misalnya seperti warnanya akan berubah mengikuti background color elemen, atau jika elemen dapat ditekan, maka padding juga termasuk area yang dapat ditekan.

    Border merupakan garis pembatas padding dengan margin, fungsinya adalah untuk memberikan batas visual pada elemen. Batas ini dapat memiliki style sendiri, tidak terpengaruh dengan objek. Dapat dilihat border berfungsi layaknya outline objek.

    Margin Merupakan area terluar, di luar border, fungsinya adalah untuk memberikan jarak antara elemen satu dengan lainnya. Area ini berguna agar elemen tidak bertabrakan sehingga lebih rapih dan mudah dilihat.

    contoh implementasinya adalah seperti `<div style="width: 200px; padding: 20px; border: 5px solid red; margin-top: 20px; ...>`, artinya elemen pada div tersebut akan memiliki ukuran interaksi (misal dapat ditekan) sebesar padding (20 pixels), dengan dibatasi outline dengan ketebalan 5 pixels dan berwarna merah seperti dengan pada border, dan berjarak 20 pixels dari elemen diatasnya.

IV. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

    Flex box merupakan one dimensional layout, yaitu layout yang berguna untuk membagi space di dalam suatu kontainer dan mengatur alignment elemen secara horizontal atau vertikal. Flex box berguna untuk mengatur komponen kecil dan style sederhana, misalnya seperti pada navigation bar dimana seluruh elemen terletak pada baris yang sama sehingga diperlukan spacing yang setara.

    Grid layout merupakan two dimensional layout, yaitu layout yang berguna untuk mengatur elemen ke dalam baris dan kolom sehingga setara secara horizontal dan vertikal. Grid layout berguna untuk mengatur layout yang bersifat kompleks dan besar, misalnya seperti gallery atau halaman utama dimana terdapat banyak elemen yang harus disusun secara rapih.

V. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step!

    1. Implementasikan fungsi untuk menghapus dan mengedit product.

        Untuk membuat fungsi hapus product, pertama dibuatlah fungsi `delete_product` dalam views.py. Fungsi ini akan mengambil parameter request dan product id. Pertama fungsi akan mencari product yang akan dihapus berdasarkan product id yang sesuai, kemudian akan menghapus product yang ditemukan dengan `product.delete()` dan mereturn HTTPsResponse ke client. Untuk mengakses fungsi, hanya perlu membuat sebuah elemen/tombol yang akan meredirect ke url penghapusan disertai dengan product id tersebut yang akan secara otomatis menghapus product dari database.

        Untuk membuat fungsi edit product, pertama dibuatlah fungsi `edit_product` dalam views.py. Fungsi ini akan mengambil parameter request dan product id. Pertama fungsi akan mencari product yang akan diedit berdasarkan product id yang sesuai, kemudian fungsi akan memanggil ProductForm dengan isian yang telah ada pada produk (instance=product). Setelah user mengisi dan submit form, akan dicek apakah form valid, jika iya maka django akan menyimpan edit dan mengganti detail produk sesuai dengan isian form tersebut. Untuk mengakses fungsi, hanya perlu membuat sebuah elemen/tombol yang akan meredirect ke url pengeditan disertai dengan product id tersebut.

    2. Kustomisasi halaman login, register, tambah product, edit product, dan detail product semenarik mungkin.

        Untuk halaman login dan register, hanya perlu menambahkan sebuah form didalam sebuah card yang akan meminta user untuk menginput username dan password. Kemudian ditambahkan sebuah tombol untuk memanggil fungsi login atau register, isi input form again digunakan untuk melakukan autentikasi. Jika autentikasi gagal, maka dibuatlah sebuah pesan dari django authentication handling kepada user.

        Untuk halaman tambah product dan edit produk, karena dapat langsung menggunakan django form builder, hanya perlu membuat sebuah card pada suatu background dan membuat tombol confirm atau cancel serta tombol return ke halaman utama. Untuk tombol add product, saya pindahkan ke navbar sehingga user dapat langsung menambahkan produk sendiri dari halaman manapun.

        Untuk detail product, halaman dibagi menjadi dua menggunakan flexbox, kemudian pada sisi kiri diletakkan gambar produk, jika produk tidak memiliki stok, maka gambar memiliki overlay "OUT OF STOCK". Jika produk merupakan milik user yang sekarang sedang login, maka terdapat juga tombol untuk mengedit dan menghapus produk langsung dari halaman detail produk.
        Pada sisi kiri, terdapat detail produk, mulai dari badges jika produk featured, memiliki stock atau tidak, dan bersifat top rated. Setelah itu terdapat juga nama produk, harga, deskripsi, informasi tambahan berupa user yang menjual, brand, stock tersisa, dan kategori. Terdapat tombol untuk add to cart dan buy now yang masih belum berfungsi, serta tombol rating dan share yang belum diimplementasikan.

    3. Kustomisasi halaman daftar product menjadi lebih menarik dan responsive.

        Karena sebelum Tugas Individu 5 saya sudah mengimplementasikan halaman utama yang ditampilkan dengan product cards, saya tinggal memindahkan kode html yang telah dibuat ke dalam product_cards.html dan menambahkan fungsionalitas tambahan seperti badge jika produk featured atau top rated, dan display rating. Saya juga menambahkan carousel yang menampilkan produk-produk yang ada pada awal halaman berdasarkan tailwind documentation di internet.
        Selain itu saya juga merapihkan halaman utama dengan menghapus header untuk menggantikannya dengan carousel, merapihkan tombol filter produk, serta memindahkan tombol add product ke bagian navbar.

    4. Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!

        Pada product_cards.html, saya menambahkan dua tombol dengan menggunakan ikon svg dari internet sebagai tombol untuk mengedit dan menghapus produk tersebut. Tombol tersebut hanya akan muncul jika user sudah terautentikasi dan merupakan penjual produk tersebut. Tombol tersebut akan redirect user untuk edit dan hapus produk, mengoverwrite card yang keseluruhannya jika ditekan akan redirect ke produk detail.

    5. Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.

        Untuk bagian navbar, saya menambahkan icon aplikasi sementara serta namanya pada bagian kiri navbar yang berguna sebagai tombol home jika ditekan. Saya juga menambahkan tombol drop down kategori yang berfungsi sebagai filter halaman utama yang akan menampilkan produk dengan kategori yang sesuai. Terdapat juga searchbar yang akan menampilkan produk yang terkait dengan input yang dimasukkan, dengan menggunakan django Q.
        Search bar akan mencari produk dengan nama, vendor, brand, dan kategori yang sama dengan yang dicari. Setelah itu terdapat tombol sell product yang berguna untuk menambahkan produk, dan pada bagian kanan terdapat bagian user dan tombol log out.

</detail>

