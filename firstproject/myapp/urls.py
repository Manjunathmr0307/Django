from django.urls import path
from .views.view_django import echo, login_view
from .views.view_django import logout_view
from .views.view_mongo import create_student, list_students, update_student, delete_student

urlpatterns = [
    path("", login_view, name="login"),
    path("echo_form/", echo, name="echo"),
    path("logout/", logout_view, name="logout"),
    path('mongo/create/', create_student),
    path('mongo/list/', list_students),
    path('mongo/update/',update_student),
    path('mongo/delete/',delete_student),
]