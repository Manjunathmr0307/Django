from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse

def deprecated_redirect(request, endpoint):
    v2_url = reverse(f'v2:{endpoint}')
    return JsonResponse({
        "message": "API v1 is deprecated. Please update to v2.",
        "redirect_to": v2_url
    }, status=301) 
