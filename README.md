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