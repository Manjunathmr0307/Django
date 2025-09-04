from django.urls import path
from . import views

urlpatterns = [
    path('hello/', lambda request: views.deprecated_redirect(request, 'hello')),
]
