from django.urls import path
from todolist.views import show_todolist, user_register, user_login, user_logout, new_task_form, change_finished_status, delete_task, show_json, add_task_ajax, delete

app_name = "todolist" # registered namespace

# Ketika href todolist di template, jangan ke argument route, tapi ke argument name dari path
urlpatterns = [
    path("", show_todolist, name="show_todolist"), # todolist/
    path("register/", user_register, name="user_register"), # todolist/register
    path("login/", user_login, name="user_login"), # todolist/login
    path("logout/", user_logout, name="user_logout"), # todolist/logout
    path("create-task/", new_task_form, name="new_task_form"), # todolist/create-task
    path("change-status/<int:pk>", change_finished_status, name="change_finished_status"), # todolist/change-status/<pk object>
    path("delete-task/<int:pk>", delete_task, name="delete_task"), # todolist/delete-task/<pk object>, untuk tugas 4
    path("json/", show_json, name="show_json"), # todolist/json
    path("add/", add_task_ajax, name="add_task_ajax"), # todolist/add_task
    path("delete/<int:pk>", delete, name="delete"), # todolist/delete/<id object> 
]