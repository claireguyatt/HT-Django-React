# django imports
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

# project imports
from .models.user_models import User
from .serializers import UserSerializer

# create a new user
@api_view(['GET', 'POST'])
def create_user(request):

    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return HttpResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
# retrieve, update, or delete a user
def user_detail(request, pk):

    try:
        user = User.objects.get(pk=pk)
    except (User.DoesNotExist, User.DoesNotExist):
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return HttpResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)

'''
# api view for get & post (retrieve/create new X object)
@api_view(['GET', 'POST'])
def X_list(request):
    if request.method == 'GET':
        Xs = X.objects.all()
        serializer = XSerializer(Xs, many=true)
        return 
    # if GET --> return JsonResponse of all Xs
    # if POST --> create & return new JsonRsponse of new X
    '''

# api view for X detail, get, put, delete (retrieve/update/delete X object)
# if GET --> return JsonResponse of object X
# if PUT --> update JsonReponse of object X & return object
# if DELETE --> delete object X, return HTTP response





