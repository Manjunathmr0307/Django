from django.http import JsonResponse

def hello_v2(request):
    return JsonResponse({"message": "Welcome to the newer version of the App"})
