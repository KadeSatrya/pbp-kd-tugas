# Link App Heroku
https://pbp-kd-tugas.herokuapp.com/todolist/

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
