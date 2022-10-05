# Link App Heroku
https://pbp-kd-tugas.herokuapp.com/todolist/

# TUGAS 4
# A. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
`{% csrf_token %}` digunakan untuk melindungi dari serangan CSRF. `{% csrf_token %}` akan menghasilkan suatu token yang akan dicocokkan dengan token request yang masuk. Bila token tidak sama, request tersebut tidak akan dijalankan. 

# B. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Ya, kita bisa membuat elemen `<form>` secara manual. Untuk membuat elemen `<form>` secara manual dibutuhkan tag `input` dan button yang memiliki type `submit` di dalam `<form>`.

# C. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Data yang disubmit pada `form HTML` akan diproses oleh `views` dan diteruskan ke `model` yang sesuai di database. Ketika ada template yang membutuhkan data tersebut, `views` akan mengambil data dari `models` dan meneruskannya ke `template` yang akan dirender. Hasilnya akan dikembalikan ke `views` yang akan mengembalikan response ke user.

# D. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

## MEMBUAT APLIKASI HINGGA MEMBUAT MODEL
1. `startapp` aplikasi `todolist` melalui cmd lalu menambahkan ke daftar `ISNTALLED_APPS` pada `settings.py`
2. Membuat method `show_todolist` pada `views.py` yang akan merender `todolist.html` yang berisi tabel isi todolist
3. Membuat `urls.py` pada folder `todolist` dan mendaftarkan nama aplikasi serta path `todolist` pada `urlapatterns`
4. Menambahkan path ke `todolist/urls.py` pada `project_django/urls.py`
5. Menambahkan class `Task` pada `models.py` yang memiliki atribut sesuai dengan yang dijelaskan di soal dan melakukan migration
6. Mengimport `Task` ke `views.py` dan menambahkan datanya sebagai salah satu `context` method `show_todolist`

## LOGIN
1. Membuat `user_login.html` yang berisi template halaman login dengan 2 kolom input dan tombol login yang menggunakan method POST
2. Menambahkan hyperlink ke tempat registrasi user pada `user_login.html`
3. Menambahkan method `user_login` pada `views.py` yang akan merender `user_login.html` dan memvalidasi user dari input yang dimasukkan, lalu redirect ke `todolist/`
4. Menambahkan path ke `user_login` pada `urlpatterns` dalam `todolist/urls.py` 
5. Merestriksi halaman `todolist` dengan menambahkan `@login_required` di atas method `show_todolist` dalam `views.py` dan mengatur url halaman login

## LOGOUT
1. Menambahkan method `user_logout` pada `views.py` yang akan melogout user dan redirect ke halaman login
2. Menambahkan path ke `user_logout` pada `urlpatterns` dalam `todolist/urls.py`

## REGISTER USER
1. Membuat template `user_register.html` yang berisi form, tombol submit, dan pesan yang ditampilkan ketika registrasi berhasil
2. Membuat method `user_register` pada `views.py` yang akan merender `user_register.html` dengan `context` berupa `UserCreationForm`
3. Menambahkan path ke `user_register` pada `urlpatterns` dalam `todolist/urls.py`


## FORM PEMBUATAN TASK
1. Membuat template `new_task_form.html` yang memiliki kolom input untuk judul dan deskripsi serta tombol submit yang menggunakan method POST
2. Membuat method `new_task_form` pada `view.py` yang akan merender `new_task_form.html` dan menciptakan  object `Task` baru sesuai input yang diberikan, lalu redirect ke halaman utama todolist
3. Menambahkan path ke `new_task_form` pada `urlpatterns` dalam `todolist/urls.py`
4. Merestriksi halaman `todolist/create-task` dengan menambahkan `@login_required` di atas method `new_task_form` dalam `views.py` dan mengatur url halaman login

## Deployment ke Heroku
1. Melakukan commit dan push ke github

# TUGAS 5

# A. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
1. Inline CSS adalah CSS yang diletakkan di dalam tag HTML. Keuntungan dari Inline CSS adalah kecepatan pengerjaan bila dilakukan dalam skala kecil. Kekurangannya adalah bila file yang dikerjakan memiliki skala yang besar, akan memakan waktu yang lama untuk mendekorasi tiap tag yang ada.

2. Internal CSS adalah CSS yang diletakkan di dalam file HTML yang sama namun berada dalam tag `<style>`. Keuntungan dari internal CSS adalah mengurangi jumlah file bila dibandingkan dengan external CSS dan mempercepat pekerjaan dalam skala besar bila dibandingkan dengan inline CSS. Kerugiannya adalah memperbesar ukuran halaman website dan memperlambat waktu loading.

3. External CSS adalah CSS yang diletakkan di dalam file CSS tersendiri yang terpisah dari file HTML. Keuntungan dari external CSS adalah mempercepat waktu pekerjaan karena style CSS dalam satu file bisa digunakan oleh beberapa file HTML. Kerugiannya adalah waktu loading yang lebih lambat karena terdapat lebih banyak file.


# B. Jelaskan tag HTML5 yang kamu ketahui.
1. `<table>` untuk mendefinisikan suatu tabel
2. `<tr>` untuk baris dalam suatu tabel
3. `<th>` untuk header cell dalam suatu baris tabel
4. `<td>` untuk data cell dalam suatu baris tabel
5. `<a>` untuk menuliskan hyperlink
6. `<form>` untuk mendefinisikan form HTML untuk menerima input
7. `<input>` untuk menerima input pengguna
8. `<title>` untuk menuliskan nama dokumen yang akan ditunjukkan
9. `<p>` untuk menuliskan suatu paragraf
10. `<head>` untuk mendefinisikan bagian head dari dokumen HTML
11. `<body>` untuk mendefinisikan bagian body dari dokumen HTML
12. `<div>` untuk mendefinisikan pembagian-pembagian dalam dokumen HTML

# C. Jelaskan tipe-tipe CSS selector yang kamu ketahui.
Selector pada CSS digunakan untuk menunjuk suatu hal pada HTML yang ingin kita ubah dengan CSS. Jenis-jenis selector yang saya ketahui adalah:

1. Element Selector yang menunjuk tag HTML. Penulisannya tidak diawali dengan tanda apapun. Contohnya bila ingin mengubah tag `<p>` maka akan dituliskan sebagai `p{}`.

2. ID Selector yang menunjuk ke ID dalam tag HTML. Penulisannya diawali dengan tanda `#`. Contohnya bila ingin mengubah `<div id="random">` maka akan dituliskan sebagai `#random{}`.

3. Class Selector yang menunjuk class dalam tag HTML. Penulisannya diawali dengan tanda `.`. Contohnya bila ingin mengubah `div class="next"` maka akan dituliskan sebagai `.class{}`.

# D. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

## Kustomisasi templat untuk halaman login, register, dan create-task
1. Menambahkan link ke bootstrap di bagian `<head>` pada `base.html` yang akan diextend oleh template html lainnya
2. Mendekorasi template `user_login.html`, `new_task_form.html`, dan `user_register.html` menggunakan CSS

## Kustomisasi halaman utama todo list menggunakan cards.
1. Mengubah struktur template `todolist.html` dari menggunakan `table` menjadi menggunakan `card` melalui `div class="card"`
2. Memasukkan tiap `task` ke dalam suatu container yang menggunakan layout `grid` dengan memasukkan `for loop` ke dalam `div` container
3. Mendekorasi template `todolist.html` menggunakan CSS

## Membuat keempat halaman yang dikustomisasi menjadi responsive.
1. Menambahkan `@media (max-width)` ke `<style>` dalam `todolist.html` untuk mengubah `grid-template-columns` yang mengatur jumlah `card` tiap baris agar menyamakan jumlah card tiap baris sesuai dengan `max-width` yang ditentukan
2. Menambahkan `@media (min-width)` ke `<style>` dalam `new_task_form.html` dan `user_login.html` untuk mengubah `width` dari `form-control` agar tidak terlalu panjang bila ukuran layar sudah melewati `min-width` yang ditentukan