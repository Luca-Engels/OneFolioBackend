from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
from bson import ObjectId
from .mongodb import users_collection, investments_collection

# Utility function to convert ObjectId to string
def obj_user_to_json(obj):
    obj['_id'] = str(obj['_id'])
    return obj
def obj_investment_to_json(obj):
    obj['_id'] = str(obj['_id'])
    obj['userId'] = str(obj['userId'])
    return obj

def user_view(request):
    users = list(users_collection.find())
    users_list = []
    for user in users:
        investments_count = investments_collection.count_documents({"userId": user["_id"]})
        user["investments"] = investments_count
        users_list.append(user)
    users = users_list
    return render(request, 'users.html', {'users': users})


@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        users = list(users_collection.find())
        print(users)
        return JsonResponse([obj_user_to_json(user) for user in users], safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        users_collection.insert_one(data)
        return HttpResponse(status=201)

@csrf_exempt
def user_detail(request, user_id):
    if request.method == 'GET':
        user = users_collection.find_one({"_id": ObjectId(user_id)})
        if user:
            return JsonResponse(obj_user_to_json(user))
        else:
            return HttpResponse(status=404)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": data})
        return HttpResponse(status=204)
    elif request.method == 'DELETE':
        users_collection.delete_one({"_id": ObjectId(user_id)})
        return HttpResponse(status=204)

@csrf_exempt
def user_by_email(request, email):
    if request.method == 'GET':
        user = users_collection.find_one({"email": email})
        if user:
            return JsonResponse(obj_user_to_json(user))
        else:
            return HttpResponse(status=404)

def investment_view(request):
    investments = list(investments_collection.find())
    investment_list = []
    for investment in investments:
        investments_count = users_collection.find({"_id": investment["userId"]})
        investment["investments"] = investments_count
        investment_list.append(investment)
    investments = investment_list
    return render(request, 'investments.html', {'investments': investments})

@csrf_exempt
def investment_list(request):
    if request.method == 'GET':
        investments = list(investments_collection.find())
        print(investments)
        return JsonResponse([obj_investment_to_json(investment) for investment in investments], safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        investments_collection.insert_one(data)
        return HttpResponse(status=201)

    
# User CRUD operations
@csrf_exempt
def investments_by_user(request, user_id):
    if request.method == 'GET':
        print(user_id)
        investments = list(investments_collection.find({"userId": ObjectId(user_id)}))
        print(investments)
        return JsonResponse([obj_investment_to_json(investment) for investment in investments], safe=False)

@csrf_exempt
def investment_detail(request, investment_id):
    if request.method == 'GET':
        investment = investments_collection.find_one({"_id": ObjectId(investment_id)})
        if investment:
            return JsonResponse(obj_investment_to_json(investment))
        else:
            return HttpResponse(status=404)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        investments_collection.update_one({"_id": ObjectId(investment_id)}, {"$set": data})
        return HttpResponse(status=204)
    elif request.method == 'DELETE':
        investments_collection.delete_one({"_id": ObjectId(investment_id)})
        return HttpResponse(status=204)
