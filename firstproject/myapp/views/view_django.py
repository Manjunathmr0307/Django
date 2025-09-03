# Logout view for session flush
def logout_view(request):
    request.session.flush()
    return render(request, "login.html", {"error": None})

# Login view for login.html
def login_view(request):
    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # Accept any username and password, no authentication
        if username and password:
            request.session["logged_in"] = True
            return render(request, "echo_form.html")
        else:
            error = "Please enter both username and password."
    return render(request, "login.html", {"error": error})
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
import json

from ..models import Student
from ..serializers import StudentSerializer


def hello(request):
    return HttpResponse("Hello, World!")

def bye(request):
    return HttpResponse("bye, World!")

@csrf_exempt
def echo(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST only'}, status=405)
    data = json.loads(request.body or '{}')
    return JsonResponse({'received': data}, status=201)

@csrf_exempt
def update_echo(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body or '{}')
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        return JsonResponse({'action': 'updated', 'received': data}, status=200)
    return JsonResponse({'error': 'PUT only'}, status=405)

@csrf_exempt
def delete_echo(request):
    if request.method == 'DELETE':
        return JsonResponse({'status': 'deleted', 'user': 'nitesh'}, status=200)
    return JsonResponse({'error': 'DELETE only'}, status=405)

@method_decorator(csrf_exempt, name='dispatch')
class SimplePostView(View):
    def post(self, request):
        data = json.loads(request.body or '{}')
        return JsonResponse({'received': data})

class DRFPostView(APIView):
    def post(self, request):
        return Response({'received': request.data})

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

def simple_page(request):
    products = [
        {'name': 'Book', 'price': 299, 'description': 'A good book'},
        {'name': 'Pen', 'price': 19, 'description': 'Blue ink pen'},
    ]
    return render(request, 'simple_products.html', {'products': products})

