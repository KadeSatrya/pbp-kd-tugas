from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Merestriksi show_todolist sehingga memerlukan login
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    """
    Method untuk merender todolist.html yang akan diisi dengan\n
    data pada todolist dan username sesuai dengan user yang telah login
    """
    todolist_data = Task.objects.filter(user = request.user)
    context = {
        "todolist_data" : todolist_data,
        "username" : request.user.get_username(),
    }
    return render(request, "todolist.html", context)


def user_register(request):
    """
    Method untuk merender user_register.html\n
    dan menerima input data user baru, lalu redirect ke halaman login
    """
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:user_login')
    
    context = {'form':form}
    return render(request ,'user_register.html', context)

def user_login(request):
    """
    Method untuk menghandle login user\n
    - Render user_login.html\n
    - Menerima input yang dimasukkan lalu memvalidasinya\n
    - Bila valid maka redirect ke halaman utama
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'user_login.html', context)

def user_logout(request):
    """Method yang akan menghandle logout user"""
    logout(request)
    return redirect('todolist:user_login')

@login_required(login_url='/todolist/login/')
def new_task_form(request):
    """
    Method yang akan menghandle pembuatan task baru\n
    - Render new_task_form.html\n
    - Membuat object Task baru dari input yang diberikan user\n
    - Redirect ke halaman utama
    """
    if request.method == "POST":
            user = request.user
            title = request.POST.get("title")
            description = request.POST.get("description")
            Task.objects.create(user = user, title=title, description=description)
            return(redirect("todolist:show_todolist"))
    return render(request, "new_task_form.html")

# TUGAS BONUS

def change_finished_status(request, pk):
    task = Task.objects.get(pk = pk)
    task.is_finished = not task.is_finished
    task.save()
    return redirect("todolist:show_todolist")

def delete_task(request, pk):
    Task.objects.get(pk = pk).delete()
    return redirect("todolist:show_todolist")