# Goal Gear

**Tautan PWS**: https://rochelle-marchia-goalgear.pbp.cs.ui.ac.id/

---

## Deskripsi singkat
Goal Gear adalah aplikasi toko perlengkapan football yang menampilkan daftar produk. Pada tugas ini saya mengimplementasikan model `Product` yang memuat atribut wajib: `name`, `price`, `description`, `thumbnail`, `category`, dan `is_featured`.

---

<details>
<Summary><b>Tugas 2</b></Summary>

## Implementasi Checklist

1. **Membuat proyek Django baru** dengan `django-admin startproject goal_gear`. 
    Sebelumnya, membuat virtual environment terlebih dahulu dan meng-activate virtual environmentnya serta menginstal dependencies (library, framework, package) yang dibutuhkan. 
    Setelah membuat proyek Django, mengonfigurasi environment variables dan production (menggunakan database dengan kredensial).
    Lalu menambahkan beberapa kode untuk menggunakan environment variables, development, serta mongonfigurasi production dan database sesuai dengan kredensial dari env.
    Menjalankan migration database dengan `python manage.py migrate` dan jalankan server Djangod dengan perintah `python manage.py runserver` agar database terinisialisasi dengan tabel-tabel default bawaan Django (seperti autentikasi, session, admin), sehingga siap digunakan sebelum menambahkan model baru.
    Deactivate virtual environment dan membuat repositori GitHuB baru bernama goal-gear (public) dan menghubungkan repositori lokal dengan repositori GitHub.
    Lakukan add, commit, dan push dari direktori repositori lokal.
    Setelah itu, create new project pada web PWS dan menyimpan credentials yang diperoleh lalu mengedit environment variables dengan yang sudah ada pada env.prod serta menambahkan URL deployment PWS pada `ALLOWED_HOSTS` di `settings.py`.
    Lakukan add, commit, dan push ke repositori GitHub.
    Menjalankan perintah yang terdapat pada Project Command di halaman PWS dan meng-enter credentials yang sudah diterima.

2. **Membuat aplikasi baru `main`** dengan `python manage.py startapp main` untuk struktur aplikasi Django.
    Sebelumnya, mengactivate environment yang telah dibuat sebelumnya.
    Setelah membuat aplikasi main, tambahkan 'main' ke dalam `INSTALLED_APPS` pada `settings.py` untuk mendaftarkan aplikasi tersebut ke dalam proyek.
    Membuat direktori baru `templates` di dalam aplikasi main untuk menampilkan data program goal gear.
    Pembuatan berkas baru `main.html` dan isi sesuai dengan data diri.
    Mengubah berkas `models.py` dalam aplikasi `main`

3. **Membuat model pada aplikasi `main` dengan nama `Product` dan memiliki atribut wajib:**
    - `name`: CharField  
    - `price`: IntegerField  
    - `description`: TextField  
    - `thumbnail`: URLField  
    - `category`: CharField  
    - `is_featured`: BooleanField
    Lalu penambahan atribut optional seperti:
    - `stock`: PositiveIntegerField
    - `brand`: CharField
    - `rating`: FloatField
    Setelah itu membuat migrasi model dengan perintah `python manage.py makemigrations` untuk menciptakan berkas migrasi yang berisi perbuahan model yang belum diaplikasikan ke dalam base data. `python manage.py migrate` untuk menerapkan migrasi ke dalam base data lokal dan mengaplikasikan perubahan model yang tercantum.

4. **Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas.**
    Lakukan `from django.shortcuts import render` yang akan digunakan untuk render tampilan HTML.
    Lalu tambahkan fungsi `show_main` yang menerima parameter `request` dengan data npm, name, class, dan app_name.
    Pada `main.htmml`, ubah nama dan kelas menjadi struktur kode Django yang sesuai untuk menampilkan data. Lalu ubah `<h1>Goal Gear</h1>` menjadi `<h1>{{ app_name }}</h1>`.
    Sintaks Django tersebut merupakan template variables yang digunakan untuk menampilkan nilai variable yang telah didefinisikan.

5. **Membuat sebuah routing pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`.**
    Sebelum itu, buat berkas `urls.py` di dalam direktori `main`. `urls.py` menautkan '' ke show_main.
    Import modul yang sesuai lalu isi `urlpatterns` dengan object `URLPATTERN` yang dihasilkan oleh fungsi `path()`.
    Pada `urls.py` dalam direktori proyek `goal-gear`, import `include` dari `django.urls`. Lalu menambahkan rute URL `path('', include('main.urls'))` di dalam list `url.patterns` untuk memastikan request root diarahkan ke view aplikasi dan halaman aplikasi main dapat diakses secara langsung.

6. **Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-teman melalui Internet**
    Deployment ke PWS dengan commit & push project ke GitHub, lalu hubungkan ke PWS agar bisa diakses online lewat dashboard PWS.

---

## Bagan Request-Response

[Client Browser]
    GET /
      |
      v
[goal_gear/urls.py]  -- include('main.urls') -->
      |
      v
[main/urls.py]  -- path('', show_main) -->
      |
      v
[main/views.py] (show_main)
  - Siapkan context (npm, name, class, app_name, products)
  - return render(request, 'main/main.html', context)
      |
      v
[main/templates/main.html]
  - Menerima context -> render HTML (menggabungkan data)
      |
      v
[HttpResponse HTML]
      |
      v
[Client Browser]  <-- tampilkan halaman

- urls.py (project & app) memetakan URL ke fungsi view.

- views.py mengandung logika: mengambil data dari models.py bila perlu, menyiapkan context dan memanggil render().

- models.py mendefinisikan struktur data / ORM yang dipetakan ke database.

- Template HTML (main.html) menerima context dari view dan menghasilkan HTML yang dikirim ke client.

---

## Peran `settings.py`

`settings.py` adalah pusat konfigurasi proyek Django. peran utamanya:
`INSTALLED_APPS`: daftar aplikasi aktif (harus berisi 'main'). Tanpa ini, model/template tidak dikenali.
`DATABASES`: konfigurasi database (sqlite/pg/mysql). Django mengarahkan semua operasi ORM ke sini.
`TEMPLATES`: konfigurasi mesin template dan lokasi template.
`STATIC_URL`: lokasi file statis (CSS/JS/images).
`ALLOWED_HOSTS`: daftar host/URL yang diizinkan ketika deploy (harus disesuaikan atau ["*"] untuk uji).
`DEBUG`: mode pengembangan vs produksi.
`MIDDLEWARE`: middleware yang memproses request/response.
`WSGI_APPLICATION`: entry point untuk server produksi (mis. Gunicorn / Daphne).
settings.py memengaruhi bagaimana aplikasi berjalan baik di lokal maupun saat deployment. Pastikan variabel sensitif (`SECRET_KEY`) tidak di-commit ke publik, hanya menggunakan environment variables untuk production.

---

## Cara Kerja Migrasi Database di Django

**Migrasi Django menyinkronkan perubahan model Python (`models.py`) ke struktur tabel database.** Alur dasarnya:
1. Tulis/ubah model di `models.py`.
2. Buat file migrasi: `python manage.py makemigrations`
   Django membandingkan model sekarang dengan terakhir yang tercatat dan membuat file migrasi Python (`migrations/0001_initial.py`, dll.) berisi operasi seperti `CreateModel`, `AddField`, `AlterField`.
3. Terapkan migrasi ke database: `python manage.py migrate`
   Django menjalankan operasi migrasi ke DB target (create table, add column, dll.) dan mencatat migrasi yang sudah dijalankan di tabel `django_migrations`.
4. Keuntungan migration:
   - Riwayat perubahan tersimpan dan dapat dikembalikan (migrate < migration).
   - Konsistensi antara model Python dan struktur DB.

Beberapa catatan:
- `makemigrations` menghasilkan file Python yang bisa direview.
- Migrasi penting saat deploy ke server karena memastikan struktur DB di server sama dengan lokal.
- Migrasi menjaga dependensi antar app dan urutan eksekusi sehingga perubahannya konsisten di lingkungan dev/staging/production.

---

## Alasan Django cocok sebagai permulaan pembelajaran framework

**Beberapa alasan praktis dan pedagogis mengapa Django cocok untuk pemula:**
- "Batteries-included" : Django menyediakan banyak komponen siap pakai (ORM, auth, admin, forms, session, middleware). Mahasiswa bisa membangun aplikasi fungsional dengan sedikit konfigurasi tambahan.
- ORM yang mudah : bekerja dengan model Python (CRUD tanpa menulis SQL), sehingga pemula bisa fokus logika aplikasi sebelum belajar SQL mendalam.
- Struktur yang konsisten : konvensi project/app membuat pemisahan tanggung jawab jelas (models, views, templates), memudahkan maintenance dan kolaborasi.
- Keamanan built-in : fitur seperti CSRF protection, XSS escaping, dan prepared statements default membantu mencegah celah umum secara out-of-the-box.
- Admin otomatis : django.contrib.admin menghasilkan panel admin CRUD hanya dengan beberapa baris konfigurasi, berguna untuk demo dan pengisian data awal.
- Dokumentasi & komunitas besar : banyak tutorial, paket, dan solusi ketika menemui masalah sehingga learning-curve terasa lebih landai.
- Cepat untuk prototyping : dalam waktu singkat kamu bisa punya aplikasi end-to-end (model → view → template → DB → deploy). Ini memotivasi pembelajaran berbasis proyek.

**Kompromi / hal yang perlu diperhatikan:**
- Django cukup “opinionated” : bagus untuk belajar pola tertentu, tapi ketika melangkah ke microframework atau arsitektur non-monolitik (mis. microservices), kamu perlu adaptasi.
- Untuk aplikasi yang sangat ringan atau real-time heavy, framework lain (Flask, FastAPI, Node.js) mungkin lebih ringkas atau lebih optimal; tapi Django tetap sangat baik sebagai fondasi belajar web development.

---

## Feedback untuk asisten dosen

Asdos menjelaskan materi dengan cukup jelas dan runtut, sehingga mudah diikuti meskipun banyak istilah baru.
Penjelasan step-by-step sangat membantu terutama saat menjalankan perintah di terminal.
Asdos juga sangat membantu pada saat trouble-shooting karena banyak mahasiswa yang masih kebingungan dengam terms-terms baru yang diajari.
Overall semua berjalan lancar meskipun ada beberapa steps yang masih terbelit-belit (ini di tutorial 0) tetapi mudah untuk dilihat di mana salahnya.

</details>

---

<details>
<Summary><b>Tugas 3</b></Summary>

## Alasan mengapa kita memerlukan data delivery dalam mengimplementasikan sebuah platform

Sebuah platform aplikasi (misalnya e-commerce, media sosial, sistem informasi kampus) pada dasarnya berfungsi untuk menghubungkan data, logika bisnis, dan pengguna. Agar platform bisa berjalan, data yang ada di server (database/backend) harus bisa dikirim (delivered) ke pengguna (client/browser/aplikasi mobile), dan sebaliknya data dari pengguna juga harus sampai ke server. Proses inilah yang disebut data delivery.
Alasannya adalah agar platform bisa berfungsi (komunikasi client-server)
    Tanpa data delivery, pengguna tidak bisa melihat informasi apa pun. Misalnya: halaman produk e-commerce hanya kosong jika data produk tidak dikirim dari server.
    Data delivery memastikan request dari client diproses -> hasilnya dikembalikan dalam bentuk response (HTML, JSON, XML, dsb).

---

## Perbandingan XML dan JSON dan Alasan JSON Lebih Populer Dibandingkan XML

JSON lebih populer dibandingkan XML karena beberapa alasan penting.
1. JSON jauh lebih ringkas sehingga data yang dikirim lebih kecil dibanding XML yang cenderung verbose dengan banyak tag.
2. JSON terintegrasi secara native dengan JavaScript sehingga mudah dipakai di web melalui `JSON.parse()` atau `JSON.stringify()`, sementara XML membutuhkan parsing tambahan.
3. Dari sisi performa, JSON lebih cepat dan sederhana untuk diproses, sedangkan XML lebih berat karena kompleksitasnya. Ekosistem modern seperti REST API, GraphQL, dan aplikasi mobile juga lebih banyak mendukung JSON sebagai standar.

Selain itu, JSON lebih aman karena XML memiliki potensi kerentanan tambahan seperti XXE jika parser tidak dikonfigurasi dengan benar. Meski begitu, XML tetap relevan untuk kasus tertentu seperti dokumen yang membutuhkan struktur kompleks, validasi dengan XSD, atau transformasi dengan XSLT. Namun, untuk kebutuhan pertukaran data modern, JSON biasanya menjadi pilihan utama karena kesederhanaa dan efisiensi.

---

## Fungsi `is_valid` Pada Form Django

**`form.is_valid()` menjalankan proses validasi seluruh form.** Secara teknis ia memanggil `full_clean()` yang:
1. Memeriksa tiap field (field validators, required, tipe data), mengubah input string menjadi nilai Python yang tepat (mis. `"123"` -> `123`).
2. Menjalankan `clean_<field>()` untuk tiap field jika ada (validasi khusus per-field).
3. Menjalankan `clean()` pada form untuk validasi lintas-field (mis. cek konsistensi antar dua field).
4. Untuk `ModelForm`, juga akan menjalankan langkah post-clean yang memeriksa validasi model (mis. `unique` constraints) dan menambahkan error bila perlu.
5. Mengisi `form.cleaned_data` (hanya ketika valid) dan `form.errors` (jika tidak valid).

Fungsi mengembalikan `True` jika semua pemeriksaan lulus, `False` jika ada error.

**Kenapa butuh `is_valid()`?**
1. Menjamin integritas data sebelum menyimpan ke database, mencegah data invalid/berbahaya disimpan.
2. Konversi & normalisasi input: memberi kamu `cleaned_data` yang siap dipakai (tipe yang benar).
3. Menjalankan validasi model (untuk `ModelForm`) sehingga constraint DB/aturan bisnis bisa dicek di tingkat aplikasi sebelum save.
4. Keamanan: mengurangi risiko input berbahaya karena validator dan mekanisme CSRF + form handling.

---

## `csrf_token`: Fungsi, Kepentingan, Keamanan

**Fungsi csrf_token**
`{% csrf_token %}` memasukkan token acak unik ke dalam form HTML (sebagai `<input name="csrfmiddlewaretoken" value="...">`) yang kemudian diverifikasi oleh Django saat form dikirim. Token ini memastikan bahwa permintaan POST berasal dari halaman yang benar (origin), bukan dari situs jahat, dengan mencocokkan token yang diberikan browser dengan token yang disimpan/diterbitkan Django.

**Mengapa diperlukan**
Tanpa token, server tidak dapat membedakan apakah permintaan yang memakai kredensial (cookie sesi) benar-benar dibuat oleh pengguna melalui halaman aplikasi kamu atau dibuat oleh pihak ketiga. `csrf_token` memutus kemampuan penyerang untuk “menggunakan” sesi pengguna yang sudah masuk untuk melakukan aksi atas nama mereka.

**Apa yang terjadi jika tidak ditambahkan**
1. Jika middleware CSRF tetap aktif tapi form tidak menyertakan token -> Django akan menolak request (HTTP 403).
2. Jika middleware CSRF dinonaktifkan atau endpoint diberi `@csrf_exempt` -> form tanpa token akan diproses, dan aplikasi menjadi rentan terhadap CSRF.

**Bagaimana penyerang memanfaatkan (contoh nyata)**
1. Korban login ke bank.`example.com` (cookie sesi tersimpan di browser).
2. Korban membuka halaman berbahaya di `attacker.com` (mis. lewat link, iklan).
3. Halaman`attacker.com` berisi form yang mengirim POST ke `https://bank.example.com/transfer/` dengan parameter transfer uang, dan diset untuk auto-submit.
4. Browser korban otomatis mengirim request ke `bank.example.com` bersama cookie sesi korban, sehingga server mengira request itu valid dari korban dan mengeksekusi transfer.
5. Jika aplikasi memeriksa CSRF token, request dari `attacker.com` gagal. Tanpa CSRF protection, penyerang berhasil.

---

## Implementasi Checklist

1. **Views untuk XML/JSON (all & by id)** pada `main/views.py`
    Pada `views.py` di direktori main, tambahkan import HttpResponse dan Serializer pada bagian paling atas.
    Kemudian tambahkan 4 fungsi:
        a. `show_xml(request)`: variabel di dalam fungsi berikut menyimpan hasil query dari seluruh data yang ada pada `Product` serta return function berupa `HttpResponse` yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML dan parameter `content_type="application/xml"`.
        b. `show_json(request)`: variabel di dalamnya menyimpan hasil query dari seluruh data yang ada pada `Product` serta return function berupa `HttpResponse` yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON dan parameter `content_type="application/json"`.
        c. `show_xml_id(request, product_id)`:  variabel di dalam fungsi tersebut yang menyimpan hasil query dari data dengan id tertentu yang ada pada `Product` serta return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML dan parameter `content_type` dengan value `"application/xml"`.
        d. `show_json_id(request, product_id)`:  variabel di dalam fungsi tersebut yang menyimpan hasil query dari data dengan id tertentu yang ada pada `Product` serta return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON dan parameter `content_type` dengan value `"application/json"`.

2. **Routing URL untuk masing-masing views**
    Pada `urls.py` yang ada di direktori `main`, import fungsi-fungsi yang sudah dibuat tadi (`from main.views import show_main, show_xml, show-json, show_xml_id, show_xml_json`) lalu tambahkan masing-masing path url ke dalam `urlpatterns` untuk akses fungsi yang sudah diimpor.

3. **Halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan di redirect ke halaman `form`, serta tombol "Detail" pada setiap data objek model**
    Pada direktori `main`, membuat berkas baru `forms.py` untuk membuat struktur form yang dapat menerima data Product baru dengan fields yang sesuai pada `models.py`.
    Lalu pada berkas `views.py` dalam direktori `main` juga, import forms dan `django.shortcuts`. Tambah fungsi `create_product(request)` yang digunakan untuk menghasilkan form untuk menghasilkan produk setelah submit form. Tambah fungsi `show_product(request)` untuk mengambil objek `Product` berdasarkan id.
    Di direktori `main` pada `views.py`, import fungsi-fungsi yang sudah dibuat tadi (`from main.views import show_main, create_product, show_product, show_xml, show-json, show_xml_id, show_xml_json`) kemudian tambah path URL ke dalam variabel `urlpatterns`.
    Pada `main.html` pada direktori `main/templates`, tambahkan kode untuk menampilkan product serta tombol "Add Product" yang akan redirect ke halaman form serta tombol "View Details" yang akan redirect ke halaman objek model.

4. **Halaman form untuk menambahkan objek model**
    Membuat berkas HTML `create_product.html` pada `main/templates` untuk halaman form.
    Form dikirim dengan metode `POST`, karena ingin mengubah database (menambah produk baru).
    `{{ form.as_table }}` menampilkan semua field dari `ProductForm` dalam bentuk tabel HTML.
    Tombol submit (`<input type="submit">`) saat diklik, data dari form akan dikirim.

5. **Halaman yang menampilkan detail dari setiap data objek model**
    Membuat berkas HTML `product_detail.html` pada `main/templates` untuk halaman detail objek.
    Tombol back (`<a href="{% url 'main:show_main' %}">`) mengarah ke halaman utama (daftar produk).
    `<h1>{{ product.name }}</h1>` menampilkan nama produk dari object product yang dikirim oleh view.
    Detail produk:
        Category selalu tampil.
        `is_featured` hanya tampil jika produk memang ditandai Featured.
        Price & Stock selalu tampil.
        Brand dan Rating hanya tampil jika datanya ada (menggunakan `{% if product.brand %}` dan `{% if product.rating %}`).
    Jika ada URL gambar (`product.thumbnail`), akan ditampilkan `<img>` dengan lebar 300px.
    Deskripsi menampilkan isi lengkap dari field `description`.

6. **Mengakses keempat URL menggunakan Postman**
    Pada aplikasi Postman, lakukan `GET` URL untuk mendapatkan detail URL xml dan json.

    1. http://localhost:8000/xml/
        ![Alt text](ScreenshotXML.png?raw=true)

    2. http://localhost:8000/json/
        ![Alt text](ScreenshotJSON.png?raw=true)

    3. http://localhost:8000/xml/[product_id]
        ![Alt text](ScreenshotXMLById.png?raw=true)

    4. http://localhost:8000/json/[product_id] 
        ![Alt text](ScreenshotJSONById.png?raw=true)

---

## Feedback asisten dosen di tutorial 2

Penjelasan yang diberikan asdos di website PBP sangat jelas dan runtut sehingga alur pengerjaan tutorial 2 mudah dipahami. Dengan adanya panduan tersebut, proses implementasi mulai dari pembuatan model, form, views, hingga routing dapat diikuti dengan baik tanpa banyak kebingungan.

</details>

---

<details>
<Summary><b>Tugas 4</b></Summary>

## Django AuthenticationForm
`AuthenticationForm` adalah form bawaan Django yang digunakan untuk proses login. Form ini berada di modul django.contrib.auth.forms dan sudah terintegrasi dengan sistem autentikasi Django.

Secara default, `AuthenticationForm` memiliki dua field utama:
`username`
`password`

Saat form divalidasi, Django otomatis mengecek apakah kombinasi username dan password cocok dengan data user yang tersimpan di database (`User` model). Kalau benar, form menghasilkan objek user yang valid, kalau salah akan mengembalikan error.

**Kelebihan `AuthenticationForm`**
1. Built-in & Terintegrasi: tidak perlu membuat form login dari nol, karena sudah disediakan oleh Django dan langsung terhubung ke sistem autentikasi (`django.contrib.auth`).
2. Validasi Otomatis: secara otomatis memvalidasi apakah username dan password benar, dan apakah akun aktif.
3. Error Handling Siap Pakai: memberikan pesan error standar (misalnya "username atau password salah") yang bisa ditampilkan di template.
4. Keamanan Tinggi: password otomatis dicek menggunakan hash (Django tidak menyimpan password plain text), sehingga lebih aman.
5. Mudah Dikustomisasi: bisa di-extend untuk menambahkan field tambahan (misalnya "remember me") atau mengubah tampilan error message.

**Kekurangan `AuthenticationForm`**
1. Terbatas pada Field Default: hanya mendukung username dan password. Jika aplikasi ingin login dengan email atau nomor HP, harus dimodifikasi.
2. Pesan Error Generik: pesan error standar mungkin terlalu sederhana untuk kebutuhan tertentu, sehingga sering perlu dikustomisasi.
3. Kurang Fleksibel untuk UI Kompleks: kalau UI butuh login modern (misalnya AJAX login, OTP, social login), form ini biasanya tidak cukup dan harus dibuat form khusus.
4. Tidak Ada "Remember Me": secara default tidak ada opsi untuk mengatur session agar tetap aktif setelah browser ditutup.

---

## Perbedaan antara autentikasi dan otorisasi

**Autentikasi (Authentication)**
Proses memverifikasi identitas pengguna, apakah benar dia adalah siapa yang dia klaim.
Contoh: user memasukkan username dan password, lalu sistem mengecek apakah cocok dengan database.
Pertanyaan yang dijawab: "Siapa kamu?"

**Otorisasi (Authorization)**
Proses menentukan hak akses user setelah berhasil terautentikasi.
Contoh: admin bisa menghapus produk, tetapi user biasa hanya bisa melihat produk.
Pertanyaan yang dijawab: "Apa yang boleh kamu lakukan?"

**Implementasi di Django**
1. Autentikasi di Django
Django menyediakan sistem autentikasi bawaan melalui `django.contrib.auth`.
    Model User: representasi pengguna (username, password, email, dll).
    Login: pakai `django.contrib.auth.authenticate()` dan `login()` untuk memverifikasi user dan menyimpannya dalam session.
    Logout: `pakai django.contrib.auth.logout()`.
    Form Bawaan: `AuthenticationForm`, `UserCreationForm`.
    Middleware: `AuthenticationMiddleware` menambahkan atribut `request.user` untuk setiap request.

Contoh:
```
from django.contrib.auth import authenticate, login

user = authenticate(request, username='rochelle', password='12345')
if user is not None:
    login(request, user)  # simpan user di session
```

2. Otorisasi di Django
Setelah user terautentikasi, Django mengecek izin user:
    Permissions: tiap model bisa punya izin (`add`, `change`, `delete`, `view`).
    Groups: kumpulan permissions yang bisa diberikan ke banyak user sekaligus.
    Decorators:
    `@login_required`: hanya user login yang bisa mengakses.
    `@permission_required('app_name.permission_code')`: hanya user dengan izin tertentu yang bisa mengakses.
    `@user_passes_test(lambda u: u.is_superuser)`: custom check.

Contoh:
```
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def dashboard(request):
    return HttpResponse("Welcome, only logged in users can see this.")

@permission_required('main.delete_product')
def delete_product(request, product_id):
    # hanya user dengan izin delete_product yang bisa mengakses
    ...
```

---

## Kelebihan dan kekurangan session dan cookie dalam konteks menyimpan state di aplikasi web

Dalam konteks menyimpan state di aplikasi web, session dan cookies memiliki perbedaan kelebihan dan kekurangan masing-masing.

Cookies menyimpan data/state langsung di sisi klien (browser). Kelebihannya, cookies sederhana, mudah digunakan, dan memungkinkan data tertentu tetap tersimpan meskipun pengguna menutup browser (persistent cookies). Namun, kekurangannya adalah kapasitas penyimpanan sangat terbatas (umumnya hanya beberapa KB per cookie), mudah dimodifikasi atau dibaca oleh pengguna, serta berisiko terhadap serangan seperti cookie theft jika tidak diamankan dengan baik (misalnya tanpa `HttpOnly` atau `Secure`).

Session, sebaliknya, menyimpan data/state di sisi server, sementara browser hanya menyimpan sebuah session ID dalam cookie. Kelebihannya, data lebih aman karena tidak langsung terlihat atau bisa diubah oleh pengguna, serta kapasitas penyimpanan bergantung pada server, bukan browser. Kekurangannya, session membebani server karena harus menyimpan data semua pengguna yang aktif, dan session biasanya hilang ketika pengguna menutup browser kecuali diatur agar lebih lama (persistent session).

Singkatnya, cookies lebih ringan tapi kurang aman, sedangkan session lebih aman tapi bisa membebani server.

---

## Apakah cookies aman secara default, apakah ada risiko potensial yang harus diwaspadai? Penanganan Django mengenai hal tersebut

**Apakah cookies aman secara default?**
Tidak sepenuhnya. Cookie standar adalah data yang disimpan di browser dan dikirim ke server pada tiap request, secara default browser tidak mengenakan proteksi tambahan. Jadi tanpa konfigurasi keamanan, cookie rentan terhadap serangan seperti XSS (pencurian cookie lewat JavaScript) dan MITM (intercept kalau koneksi tidak lewat HTTPS).

**Risiko utama saat menggunakan cookies**
a. XSS (Cross-Site Scripting): penyerang menyisipkan skrip jahat yang membaca cookie (jika cookie tidak `HttpOnly`) dan mengirimkannya ke penyerang.
b. CSRF (Cross-Site Request Forgery): cookie sesi otomatis dikirim oleh browser sehingga request jahat dari situs lain dapat beraksi atas nama user jika tidak ada proteksi CSRF.
c. Pengintaian / MITM: jika tidak pakai HTTPS, cookie bisa disadap di jaringan.
d. Manipulasi/peek: cookie yang tidak disign atau dienkripsi dapat dibaca atau diubah (client-side).
e. Ukuran & performa: cookie dikirim di setiap request, jadi payload besar memperlambat transfer.

**Bagaimana Django menangani dan fitur keamanannya**
Django membantu mengurangi risiko lewat beberapa mekanisme konfigurasi dan built-in features:
    - Session backend (default: server-side): Django menyimpan data session di server (`django.contrib.sessions`), cookie di browser hanya menyimpan session id, bukan data user. Ini jauh lebih aman daripada menyimpan data sensitif dalam cookie.
    - Signing: Bila kamu menggunakan `SignedCookieSession` atau `response.set_signed_cookie()`, Django menandatangani cookie menggunakan `SECRET_KEY` sehingga client tidak bisa memodifikasi tanpa terdeteksi (tapi isi masih terbaca karena bukan terenkripsi).
    - CSRF protection: `CsrfViewMiddleware` + `{% csrf_token %}` mencegah CSRF pada POST/unsafe methods.
    - Session rotation on login: `django.contrib.auth.login()` memanggil `rotate_token()` untuk mengurangi risiko session fixation.
    - Pengaturan cookie flags (dikonfigurasi di `settings.py`):
        `SESSION_COOKIE_SECURE = True` -> cookie hanya dikirim lewat HTTPS.
        `SESSION_COOKIE_HTTPONLY = True` -> JavaScript tidak bisa mengakses cookie sesi.
        `SESSION_COOKIE_SAMESITE = 'Lax'` (atau `'Strict'`) → mengurangi CSRF lewat cross-site requests.
        `CSRF_COOKIE_SECURE = True`, `CSRF_COOKIE_SAMESITE = 'Lax'` untuk cookie CSRF.
    - SecurityMiddleware & HSTS: `SecurityMiddleware` + `SECURE_HSTS_SECONDS` memaksa HTTPS dan mencegah downgrade.
    - Template auto-escaping: Django templates escape output default sehingga mengurangi XSS risk.

---

## Implementasi Checklist

1. **Implementasi fungsi registrasi, login, dan logout**
    Dengan mengimplementasi login, pengguna diharuskan melakukan login terlebih dahulu agar mendapatkan akses halaman utama `main`.

    Membuat fungsi dan form registrasi:
    Tambahkan beberapa import seperti `UserCreationForm` (import formulir bawaan yang memudahkan pembuatan form register pengguna) dan `messages` pada `views.py` di `main`.
    Menambahkan fungsi `register` di `views.py` untuk menghasilkan form registrasi secara otomatis dan akan membuat akun user ketika data disubmit dan melakukan redirect setelah data form disimpan.
    Buat file baru `register.html` pada `main/templates` yang berisi halaman registrasi. File ini mewarisi base.html, mengisi judul halaman lewat blok `meta`, lalu menampilkan form pendaftaran dan pesan notifikasi.
    Pada `urls.py` di direktori `main`, import fungsi yang sudah dibuat dan tambah `path url` ke dalam `urlpatterns`.

    Membuat fungsi login:
    Pada `views.py` di direktori `main`, tambah import `authenticate`, `login`, dan `AuthenticationForm`.
    Tambahkan fungsi `login_user` untuk mengautentikasi user yang mau login. Fungsi ini menangani proses login: kalau ada input POST -> validasi form -> login user -> redirect ke halaman utama.
    Membuat file `login.html` pada `main/templates` yang berisi template yang menampilkan halaman login dengan: Template ini menampilkan halaman Login dengan: form login (username + password), proteksi CSRF, pesan error/success jika ada, link menuju halaman Register, tampilan mengikuti struktur utama dari `base.html`.
    Pada `urls.py` di direktori `main`, import fungsi yang sudah dibuat dan tambah `path url` ke dalam `urlpatterns`.

    Membuat fungsi logout:
    Pada `views.py` di direktori `main`, tambah import `logout`.
    Tambah fungsi `logout_user` yang digunakan untuk menghapus sesi pengguna yang saat ini masuk dan mengarahkan ke halaman login.
    Pada `main.html` di `main/templates` tambahkan logout button.
    Buka `urls.py` pada direktori `main` dan import fungsi yang sudah dibuat dan tambah `path url` ke dalam `urlpatterns`

    Merestriksi akses halaman main dan product description:
    Pada `views.py` di direktori `main`, tambah import `login_required`.
    Tambah potongan kode `@login_required(login_url='/login')` di atas fungsi `show_main` dan `show_product`.

2. **Membuat dua akun user dengan masing-masing tiga dummy data untuk setiap akun di lokal**
    Akun 1:
        Username: iniakunrochelle
        Password: ~GUR478h
    Akun 2:
        Username: inibukanakunrochelle
        Password: AvDx_4$5

3. **Menghubungan model `Product` dengan `User`**
    Pada `models.py` di subdirektori `main`, import `from django.contrib.auth.models import User`.
    Pada model `Product` yang sudah dibuat, tambahkan kode `user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)` Jika user A membuat produk, maka user akan terisi dengan A. Jika A dihapus, semua produknya juga otomatis terhapus.
    Buat file migrasi dengan `python manage.py makemigrations` dan migrasi model dengan `python manage.py migrate` karena setiap kali melakukan perubahan pada model, harus melakukan migrasi untuk menetapkan perubahan yang dilakukan.
    Pada `views.py` di direktori `main`, ubah fungsi `create_news`. Form diisi user -> diverifikasi -> simpan data ke database sambil mencatat siapa pembuatnya (`request.user`). Kalau berhasil, balik ke halaman utama. Kalau gagal/pertama kali buka, tampilkan halaman form.
    Modifikasi fungsi `show_main`. View show_main ini menampilkan halaman utama yang berisi daftar berita (`news_list`). User bisa memilih apakah mau melihat semua berita atau hanya berita yang dia buat sendiri. Selain itu, halaman juga menampilkan identitas user yang sedang login (username, last login, dll).
    Menambahkan tombol filter My dan All pada `main.html` di `main/templates`.
    Tampilkan nama author di `news_details.html` pada `main/templates`.

4. **Menampilkan detail info user yang sedang logged in (username) dan cookies (last_login) pada halaman utama**
    Pada `views.py` di subdirektori `main`, fungsi `show_main` dimodifikasi `context`-nya dengan `'name': request.user.username`. menampilkan detail informasi user yang sedang login (username). Misalnya kalau login sebagai A, maka di halaman utama nanti variabel `{{ name }}` di template akan berisi A.
    Untuk mengambil cookie `last_login`, harus implemeentasi data dari cookies terlebih dahulu.
    Pada `views.py` di subdirektori `main`, tambah import `HttpResponseRedirect`, `reverse`, dan `datetime`.
    Pada fungsi `login_user`, tambahkan logika untuk menyimpan cookie bernama `last_login` yang menyimpan waktu terakhir pengguna berhasil masuk. Nilai timestamp ini bisa diambil saat proses autentikasi sukses. Jadi, di dalam blok `if form.is_valid():`, kodenya diganti atau ditambahkan seperti berikut.
    ```
    ...
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    ...
    ```
    Setelah user berhasil login, ia diarahkan ke halaman utama (`show_main`) dengan cookie tambahan yang berisi timestamp login.
    Pada fungsi `show_main`, tambah potongan kode `'last_login': request.COOKIES.get('last_login', 'Never')` di variable `context`.
    Mengubah fungsi `logout_user` untuk menghapus cookie `last_login` jika user melakukan logout.
    Tambahkan potongan kode `<h5>Sesi terakhir login: {{ last_login }}</h5>` pada `main.html` di direktori `main/templates` setelah tombol logout untuk menampilkan waktu terakhir user login.

</details>

---

<details>
<Summary><b>Tugas 5</b></Summary>

## Urutan prioritas pengambilan CSS selector

Urutan prioritas CSS, atau yang sering disebut specificity, menentukan aturan mana yang diterapkan ketika ada beberapa selector yang menargetkan elemen HTML yang sama. Prioritas tertinggi dimiliki oleh inline style, yaitu CSS yang ditulis langsung di atribut `style` pada elemen. Selanjutnya, selector berdasarkan ID memiliki prioritas lebih tinggi dibandingkan selector lain seperti class, atribut, atau pseudo-class. Selector berbasis class, atribut, atau pseudo-class menempati tingkat prioritas menengah, sedangkan element selector** atau pseudo-element berada di urutan paling rendah. Selain itu, jika terdapat aturan dengan !important, properti tersebut akan menimpa hampir semua aturan lain, kecuali ada inline style yang juga menggunakan !important. Terakhir, jika dua aturan memiliki tingkat specificity yang sama, maka aturan yang muncul terakhir dalam file CSS akan diterapkan pada elemen tersebut. Dengan memahami urutan ini, kita bisa mengatur tampilan elemen HTML secara konsisten dan menghindari konflik antar CSS.

---

## Pentingnya responsive design dalam pengembangan aplikasi web dan contohnya

Responsive design penting karena web sekarang diakses dari perangkat yang beragam, ponsel, tablet, laptop, bahkan TV, sehingga tampilan dan fungsi harus menyesuaikan agar pengalaman pengguna tetap konsisten dan nyaman. Tanpa responsive design, pengguna mobile akan kesulitan membaca, menavigasi, dan menyelesaikan tugas (mis. checkout, isi formulir), yang berarti hilangnya trafik, penurunan konversi, dan citra merek yang kurang profesional.

**Contoh kenapa penting:**
1. Akses & jangkauan: desain responsif membuat satu situs bisa dipakai di banyak perangkat tanpa versi terpisah.
2. Pengalaman pengguna (UX): tata letak yang adaptif, tombol cukup besar untuk sentuhan, teks yang mudah dibaca meningkatkan keterlibatan.
3. SEO & discoverability: mesin pencari memprioritaskan pengalaman mobile (mobile-first indexing), jadi situs responsif cenderung mendapat peringkat lebih baik.
4. Pemeliharaan lebih sederhana: satu basis kode/front-end yang responsif lebih mudah dirawat dibandingkan banyak versi desktop/mobile.
5. Performa & konversi: desain responsif yang dioptimalkan berperan pada kecepatan muat dan tingkat konversi.

**Contoh aplikasi/situs yang sudah menerapkan responsive design (alat populer yang umumnya responsif) dan alasannya:**
1. Airbnb: tampilan beradaptasi apik di layar kecil maupun besar; fokus pada booking cepat dan foto besar membuat UX konsisten.
2. Wikipedia: layout teks dan nav yang adaptif sehingga mudah dibaca di ponsel; prioritas konten membuatnya efektif.
3. Gmail (web): antarmuka menyesuaikan kolom dan daftar, tetap bisa membaca/membalas email di ponsel tanpa perlu aplikasi native.
Alasan mereka responsif: target pengguna luas, tujuan interaksi singkat/sering di mobile, dan pentingnya konversi/retensi.

**Contoh aplikasi/situs yang sering tidak sepenuhnya responsif dan kenapa:**
1. Situs pemerintahan/instansi lama: banyak masih menggunakan template lawas atau sistem CMS kustom; anggaran & prioritas membatasi redesign.
2. Aplikasi enterprise/ERP lama (mis. antarmuka SAP klasik atau aplikasi internal tertentu): dibuat untuk desktop dengan workflow kompleks, migrasi ke UI responsif mahal dan butuh pengembangan besar.
3. Beberapa toko online kecil yang belum update: pemilik belum memprioritaskan UX mobile atau pakai template lama. Alasan tidak responsif: keterbatasan anggaran, dependensi pada sistem lawas, kebutuhan fitur kompleks yang sulit dipadatkan ke layar kecil, atau target audiens yang dominan desktop.

---

## Margin, border, dan padding: cara mengimplementasikan ketiga hal tersebut

**Perbedaan singkat**
- Padding adalah ruang di dalam elemen antara isi (content) dan batas (border). Padding menambah area latar / background elemen.
- Border adalah garis di luar padding yang mengelilingi elemen — terlihat jika Anda beri `border-style`/`border-width`.
- Margin adalah ruang di luar border yang memisahkan elemen dengan elemen lain (atau tepi kontainer). Margin tidak berwarna oleh background elemen.

Secara urut dari dalam ke luar: content -> padding -> border -> margin.

**Point penting**
- Padding dan border mempengaruhi ukuran kotak kecuali jika `box-sizing`: `border-box`; (dengan `border-box`, lebar/tinggi yang Anda set sudah termasuk padding+border).
- Margin vertikal antar elemen blok dapat collapse (bergabung) — catatan untuk layout.
- Border butuh `border-style` (mis. solid) agar muncul.

**Contoh implementasi (html + css)**
html:
```
<div class="card">
  <p>Isi elemen (content)</p>
</div>
```

css:
```
.card {
  /* ukuran & background */
  width: 300px;
  background: #fff;

  /* padding = ruang di dalam (atas-kanan-bawah-kiri) */
  padding: 16px 24px; /* shorthand: padding: top/right-bottom/left */

  /* border = garis di luar padding */
  border: 2px solid #5459AC;
  border-radius: 8px;

  /* margin = ruang di luar border */
  margin: 24px auto; /* 24px vertikal, auto horizontal (center) */

  /* box sizing yang direkomendasikan */
  box-sizing: border-box;
}
```

**Contog pengaturan tiap sisi**
css:
```
/* padding tiap sisi */
padding-top: 8px;
padding-right: 12px;
padding-bottom: 8px;
padding-left: 12px;

/* border tiap sisi */
border-top: 1px solid #ccc;
border-left-width: 2px;

/* margin tiap sisi */
margin-top: 16px;
margin-right: 0;
margin-bottom: 16px;
margin-left: 0;
```

---

## Konsep flex box dan grid layout beserta kegunaannya

**Flexbox (Flexible Box):** cara mengatur tata letak satu dimensi (baris atau kolom). Flexbox membuat item anak dalam sebuah kontainer bisa tumbuh, menyusut, dan ter-distribusi secara mudah: Anda mengatur arah (`row`/`column`), perataan utama (`justify-content`) dan perataan silang (`align-items`), lalu tiap item bisa diberi `flex` (mis. `flex: 1`) untuk mengisi ruang. Kegunaannya: menyusun bar navigasi, tombol aksi, baris kartu yang butuh distribusi ruang dinamis, membuat kolom dengan tinggi sama, atau membuat elemen tetap center baik horizontal maupun vertikal. Singkat: fleksibel untuk layout linear/komponen.

**Grid Layout (CSS Grid):** sistem dua dimensi (baris dan kolom) untuk membangun tata letak halaman yang lebih kompleks. Dengan Grid Anda mendefinisikan baris/kolom di kontainer (`grid-template-columns/rows`), menempatkan item ke sel atau area (`grid-column`, `grid-row`), dan mengontrol gap antar sel. Kegunaannya: layout halaman besar (header/sidebar-content-footer), galeri gambar berstruktur, dashboard, atau layout responsif yang berubah secara signifikan di breakpoint. Singkat: kuat untuk grid/area 2D dan posisi presisi.

**Kapan pakai yang mana**
- Pakai Flexbox untuk susunan linier/komponen di dalam satu baris atau satu kolom (alignment, distribusi ruang, item yang harus menyesuaikan ukuran).
- Pakai Grid untuk layout halaman dua dimensi atau ketika Anda butuh kontrol explicit atas baris dan kolom sekaligus.
- Kombinasikan: seringkali container utama dibuat dengan Grid, lalu tiap cell/komponen diatur dengan Flexbox.

**Keunggulan:** Flexbox lebih mudah dan cepat untuk alignment/flow linear, Grid lebih ekspresif untuk tata letak kompleks dan responsif.

---
## Implementasi Checklist

1. **Implementasi fungsi menghapus dan mengedit product**
    Pada `views.py` di subdirektori `main`, buat fungsi baru `edit_news` dengan parameter `request`.
    Buat berkas `edit_news.html` pada `main/templates`. Ini adalah template Django untuk halaman edit product, yang menampilkan form HTML dari objek `form` untuk mengubah data product dan mengirimkannya dengan metode POST.
    Pada `urls.py` di subdirektori `main`, dan import fungsi yang sudah dibuat serta tambah path ke dalam urlpatterns untuk akses fungsi.
    Di `main.html` yang berada pada subdirektori `main/templates`, perbarui potongan kode untuk memunculkan edit pada setiap product.

    Pada `views.py` di subdirektori `main`, buat fungsi baru `delete_news` dengan parameter `request` dan `id` untuk delete data product.
    Pada `urls.py` di subdirektori `main`, dan import fungsi yang sudah dibuat serta tambah path ke dalam urlpatterns untuk akses fungsi.
    Di `main.html` yang berada pada subdirektori `main/templates`, perbarui potongan kode untuk memunculkan 'delete' pada setiap product.

2. **Kustomisasi design pada template HTML yang telah dibuat menggunakan CSS menggunakan Tailwind**
    1. Kustomisasi halaman login dan register
        Halaman login dan register telah didesain mengikuti tema aplikasi dengan kombinasi warna ungu dan biru. Form login/register memiliki border, shadow, dan padding yang nyaman untuk input, serta tampilan tombol yang responsif saat di-hover. Hal ini membuat pengguna dapat dengan mudah memahami area input dan melakukan autentikasi.

        Pengguna membuka halaman login (/login/).
        Form login menampilkan input username/email dan password dengan styling tema ungu-biru, border, padding, dan shadow.
        Tombol login memiliki efek hover untuk memberikan feedback visual.
        Jika user belum memiliki akun, bisa klik link ke halaman register.
        Halaman register (/register/) menampilkan form pembuatan akun dengan styling yang konsisten.

    2. Kustomisasi halaman tambah dan edit product
        Halaman `create_product` dan `edit_product` menampilkan form dalam box putih dengan border dan rounded corners, dilengkapi shadow lembut untuk memberi efek fokus. Setiap field form diberi padding, border, dan warna latar yang konsisten dengan tema aplikasi, sehingga pengguna jelas mengetahui area input dan dapat mengisi atau memperbarui data produk dengan nyaman. Halaman edit hanya mengubah data produk yang sudah ada, tidak menambahkan produk baru.

        - Create Product:
            Buat template `create_product.html` yang mengikuti tema warna aplikasi (ungu-biru), box putih dengan border dan shadow.
            Loop tiap field form untuk styling tiap input (padding, border, rounded corners, focus outline).
            Tambahkan tombol Publish Product dan tombol Cancel.
            Setelah submit, simpan ke database dengan `form.save(commit=False)` dan set `user=request.user`.

        - Edit Product:
            Gunakan ProductForm(`instance=product`) agar form sudah terisi data lama.
            Template sama seperti `create_product.html`, hanya tombol submit diganti menjadi Update Product.
            Setelah submit, form akan mengupdate data di database dengan `form.save()`.

    3. Kustomisasi halaman detail product
        Halaman detail product menampilkan semua informasi produk secara lengkap: nama, kategori, harga, deskripsi, stok, brand, dan thumbnail. Jika produk termasuk featured, ditandai dengan label yang menonjol. Layout halaman tetap responsif, sehingga tampilan tetap rapi baik di desktop maupun mobile.

        Pengguna klik nama atau gambar produk dari daftar produk.
        Halaman detail menampilkan informasi lengkap: thumbnail, nama, kategori, harga, deskripsi, stok, brand.
        Jika produk featured, label "Featured" ditampilkan dengan warna mencolok.
        Tombol Edit hanya muncul jika produk milik pengguna yang login.
    
    4. Halaman daftar product
        Pisahkan featured products dan normal products untuk ditampilkan di home.
        Jika query filter atau search aktif, tampilkan semua produk sesuai filter, tanpa memunculkan featured.
        Template menampilkan produk dalam bentuk card.
        Card berisi thumbnail, nama, kategori, harga.
        Card featured lebih besar dan mencolok.
        Tambahkan tombol Edit dan Hapus di setiap card.
        Jika tidak ada produk, tampilkan ilustrasi dan pesan No Products Found.
        Layout grid responsive menggunakan Tailwind grid-cols-* untuk mobile dan desktop.

        Tanpa Produk: Jika belum ada produk yang tersimpan, halaman menampilkan ilustrasi dan pesan “No Products Found” agar pengguna mengetahui kondisi kosongnya daftar produk.

        Dengan Produk: Produk ditampilkan menggunakan card yang menarik, berbeda dari desain tutorial, menampilkan thumbnail, nama, kategori, harga, dan label "featured" bila relevan. Halaman home menunjukan produk "featured" dengan size yang lebih besar dan mencolok lalu di bagian bawahnya adalah produk biasa.

        Action Buttons: Setiap card memiliki tiga tombol, View untuk melihat deskripsi produk, Edit untuk memperbarui data produk, dan Delete untuk menghapus produk tersebut (edit dan delete hanya ada pada produk milik pengguna yang sedang login). Layout card responsive sehingga tampilan tetap rapi di berbagai ukuran layar.

        Produk per-category: Produk yang ditampilkan akan sesuai dengan kategori masing-masing produk dan halaman akan berbeda dengan home karena produk "featured" akan berukuran sama dengan produk biasa lainnya.

    5. Responsive Navigation bar
        Navbar dibuat responsif terhadap perbedaan ukuran layar. Pada desktop, menu lengkap terlihat horizontal, sedangkan di mobile, menu disederhanakan dengan tombol yang dapat diklik (hamburger) untuk menampilkan opsi. Navbar juga memuat filter cepat untuk mencari per-kategori serta navigasi ke fitur lain (Add product, Keranjang, User yang sedang login serta cookiesnya, dan tombol Logout), memudahkan pengguna dalam menjelajahi aplikasi.

        Buat partial template `navbar.html.
        Tambahkan menu horizontal untuk desktop, dan menu collapsible untuk mobile.
        Tambahkan link ke filter produk (`All Products`, `My Products`) dan halaman utama.
        Gunakan Tailwind responsive classes (`sm`:, `md`:, `lg`:) untuk menyesuaikan ukuran device.
        Include navbar.html di semua template dengan `{% include 'navbar.html' %}`.

</details>

---