import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.db import models
from . import auth


@csrf_exempt
def login_user(request):
    body = json.loads(request.body)
    username = body['username']
    password = body['password']

    user = User.objects.filter(models.Q(username=username)).first()
    if not user:
        return JsonResponse({
            'errors': 'Invalid credentials',
        }, status=401)

    if not user.is_active or not user.check_password(password):
        return JsonResponse({
            'errors': 'Inactive user',
        }, status=401)

    token = auth.encode_user(user).decode('utf-8')
    return JsonResponse({
        'token': token,
    })


@csrf_exempt
def get_user(request):
    user = request.user
    return JsonResponse({
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
    }, status=200)

