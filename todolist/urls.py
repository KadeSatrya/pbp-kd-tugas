from django.urls import path
from todolist.views import show_todolist, user_register, user_login, user_logout, new_task_form, change_finished_status, delete_task

app_name = "todolist" # registered namespace

# Ketika href todolist di template, jangan ke argument route, tapi ke argument name dari path
urlpatterns = [
    path("", show_todolist, name="show_todolist"), # todolist/
    path("register/", user_register, name="user_register"), # todolist/register
    path("login/", user_login, name="user_login"), # todolist/login
    path("logout/", user_logout, name="user_logout"), # todolist/logout
    path("create-task/", new_task_form, name="new_task_form"), # todolist/create-task
    path("change-status/<int:pk>", change_finished_status, name="change_finished_status"),
    path("delete/<int:pk>", delete_task, name="delete_task")
]