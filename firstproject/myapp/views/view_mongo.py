from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from pymongo import MongoClient

def get_mongo_collection():
    client = MongoClient("mongodb://localhost:27017")
    db = client["djangodb"]
    return db["djangocl"]

@csrf_exempt
def create_student(request):
    if request.method == "POST":
        data = json.loads(request.body)
        students = get_mongo_collection()
        students.insert_one(data)
        return JsonResponse({"status": "inserted"}, status=201)

def list_students(request):
    students = get_mongo_collection()
    data = list(students.find({}, {"_id": 0}))
    return JsonResponse({"students": data})

@csrf_exempt
def update_student(request):
    if request.method == "PUT":
        data = json.loads(request.body)
        students = get_mongo_collection()
        students.update_one({"name": data["name"]}, {"$set": {"age": data["age"]}})
        return JsonResponse({"status": "updated"})

@csrf_exempt
def delete_student(request):
    if request.method == "DELETE":
        data = json.loads(request.body)
        students = get_mongo_collection()
        students.delete_one({"name": data["name"]})
        return JsonResponse({"status": "deleted"})
