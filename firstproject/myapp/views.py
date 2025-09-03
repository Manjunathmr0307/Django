from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect
import json
from .models import Echo   
def login_view(request):
    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # Accept any username and password, no authentication
        if username and password:
            request.session["logged_in"] = True
            return redirect("echo_form")
        else:
            error = "Please enter both username and password."
    return render(request, "login.html", {"error": error})

def logout_view(request):
    request.session.flush()

from .views.view_django import *
from .views.view_mongo import *