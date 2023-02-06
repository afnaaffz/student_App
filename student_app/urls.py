from django.urls import path

from student_app import views

urlpatterns= [
   path("", views.indexx, name="indexx"),
   path("index", views.index, name="index"),
   path("login_page",views.login_page,name="login_page"),


   path("adminbase", views.adminbase, name="adminbase"),
   path("students_data", views.students_data, name="students_data"),
   path("admin_register", views.admin_register, name="admin_register"),
   path("add_mark", views.add_mark, name="add_mark"),
   path("view_mark", views.view_mark, name="view_mark"),
   path("edit_view_mark/<int:id>/", views.edit_view_mark, name="edit_view_mark"),

   path("studentbase", views.studentbase, name="studentbase"),
   path("student_register", views.student_register, name="student_register"),
   path("personal_details", views.personal_details, name="personal_details"),
   path("edit_personal_details/<int:id>/", views.edit_personal_details, name="edit_personal_details"),



]

