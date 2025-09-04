from django.urls import path
from . import views

app_name = "v2"

urlpatterns = [
    path('hello/', views.hello_v2, name='hello'),
]
