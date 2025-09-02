from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import viewsets


def hello(request):
    return JsonResponse({"message": "Hello, world!"})


'''@csrf_exempt
def create_post(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Parse JSON body
            return JsonResponse({
                "status": "success",
                "message": "Post created!",
                "data": data
            })
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Invalid request method."}, status=405)


@csrf_exempt
def create_put(request):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)  # Parse JSON body
            return JsonResponse({
                "status": "success",
                "message": "Data updated!",
                "data": data
            })
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Invalid request method."}, status=405)


@csrf_exempt
def create_delete(request):
    if request.method == "DELETE":
        try:
            data = json.loads(request.body) if request.body else {}
            return JsonResponse({
                "status": "success",
                "message": "Post deleted!",
                "data": data
            })
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Invalid request method."}, status=405)


'''

@method_decorator(csrf_exempt, name="dispatch")
class Echo(View):
    storage = []     
    counter = 1      

    def post(self, request):
        """Create (POST)"""
        try:
            data = json.loads(request.body or "{}")
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        item = {"id": Echo.counter, **data}
        Echo.storage.append(item)
        Echo.counter += 1

        return JsonResponse({
            "action": "create",
            "status": "success",
            "data": item
        })

    def put(self, request):
        try:
            data = json.loads(request.body or "{}")
            item_id = data.get("id")
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        if not item_id:
            return JsonResponse({"error": "ID is required for update"}, status=400)

        for i, item in enumerate(Echo.storage):
            if item["id"] == item_id:
                Echo.storage[i].update(data) 
                return JsonResponse({
                    "action": "update",
                    "status": "success",
                    "data": Echo.storage[i]
                })

        return JsonResponse({"error": "Item not found"}, status=404)

    def delete(self, request):
        try:
            data = json.loads(request.body or "{}")
            item_id = data.get("id")
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        if not item_id:
            return JsonResponse({"error": "ID is required for delete"}, status=400)

        for i, item in enumerate(Echo.storage):
            if item["id"] == item_id:
                removed = Echo.storage.pop(i)
                return JsonResponse({
                    "action": "delete",
                    "status": "success",
                    "removed": removed
                })

        return JsonResponse({"error": "Item not found"}, status=404)

    def get(self, request):
        return JsonResponse({
            "action": "read",
            "status": "success",
            "data": Echo.storage
        })

def echo_form(request):
    return render(request,"echo_form.html")

class StudentViewSet(viewsets.ModelViewSet):
    from .models import Student
    from .serializers import StudentSerializer

    queryset = Student.objects.all()
    serializer_class = StudentSerializer