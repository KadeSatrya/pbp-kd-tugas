# Link App Heroku
https://pbp-kd-tugas.herokuapp.com/todolist/

# A. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Synchronous programming adalah jenis pemrograman di mana request diproses satu per satu. Jika user ingin melakukan suatu hal setelah mengirim request, maka user harus menunggu hingga request tersebut selesai diproses dan hasilnya dikembalikan.

Asynchronous programming adalah jenis pemrograman di mana program masih responsif meskipun sedang memproses request. Jika user sudah mengirim request,user masih bisa melakukan hal lain, seperti mengirim request baru, meskipun request sebelumnya belum selesai diproses.

# B. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-driven programming adalah paradigma pemrograman di mana alur kerja program diatur oleh terjadinya suatu event. Contoh penerapannya pada tugas ini adalah ketika user menekan tombol "Add Task (AJAX)" atau tombol "Delete" yang akan menjadi event.

# C. Jelaskan penerapan asynchronous programming pada AJAX.
AJAX adalah suatu teknik penggunaan JavaScript sehingga berjalan secara asynchronous meskipun bisa juga bisa secara synchronous. JavaScript akan mengirimkan request ke server yang akan diproses dan mengembalikan hasilnya. Halaman kemudian akan berubah sesuai dengan hasil request. Namun, yang direload hanyalah bagian yang berhubungan dengan hasil request, bukan seluruh halamannya.

# D. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

## AJAX GET
1. Membuat fungsi show_json pada views.py yang akan mengembalikan isi dari data Todolist dalam bentuk json
2. Mengatur Path fungsi show_json pada urls.py
3. Meletakkan Scripts Ajax di base.html
4. Membuat fungsi yang menggunakan Ajax Get di dalam Scripts pada block meta todolist.html
5. Fungsi tersebut akan mengambil data json dari show_json
6. Data yang didapatkan akan dipetakan ke dalam bentuk card lalu akan diappend ke container card dengan id "todolist"

## AJAX POST
1. Meletakkan scripts bootstrap di bagian body base.html
2. Membuat modal menggunakan class modal bootstrap dengan header dan body
3. Membuat form dalam body modal yang mengambil input judul dan deskripsi dengan tombol submit di paling bawah
4. Membuat fungsi JavaScript yang akan mengirimkan input dari form ke fungsi di views.py menggunakan AJAX POST
5. Membuat fungsi add_task_ajax pada views.py yang akan membuat object Task sesuai dengan data yang dikirim fungsi JavaScript
6. Fungsi tersebut akan mengembalikan JsonResponse yang berisi nilai atribut-atribut dari object Task yang dibuat
7. Membuat path untuk fungsi add_task_ajax di urls.py
8. Fungsi JavaScript yang telah dibuat akan menerima JsonResponse dan memetakan isinya ke card seperti pada AJAX GET
9. Menambahkan `data-bs-dismiss="modal"` pada tombol submit agar modal ditutup setelah menekan tombol tersebut