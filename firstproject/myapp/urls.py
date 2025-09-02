from django.urls import path, include
from django.shortcuts import render
from rest_framework.routers import DefaultRouter
from . import views
from .views import Echo, echo_form, StudentViewSet


router = DefaultRouter()
router.register(r'students', StudentViewSet)


urlpatterns = [
    path("hello/", views.hello, name="hello"),
    path("echo/", Echo.as_view(), name="echo"),
    path("form/", echo_form, name="echo_form"),
    path('', include(router.urls)),

]
