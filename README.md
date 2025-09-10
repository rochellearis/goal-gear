# Goal Gear

**Tautan PWS**: https://rochelle-marchia-goalgear.pbp.cs.ui.ac.id/

---

## Deskripsi singkat
Goal Gear adalah aplikasi toko perlengkapan football yang menampilkan daftar produk. Pada tugas ini saya mengimplementasikan model `Product` yang memuat atribut wajib: `name`, `price`, `description`, `thumbnail`, `category`, dan `is_featured`.

---

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

---