from rest_framework.decorators import api_view
from .models import RydeUser
from rest_framework.views import APIView
from rest_framework import views, status
from rest_framework.response import Response
from django.conf import settings
from rest_framework import status
from random import randint
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.http import FileResponse
from django.views.decorators.csrf import csrf_exempt
from geopy.distance import great_circle
from geopy import distance
import requests
import geopy.distance
import random
import string
import os
# Create your views here.


class SignupRydeUserView(APIView):
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')

        if not name or not email or not phone_number or not password:
            return JsonResponse({'error': 'All fields are required'}, status=400)

        # Check if the email is already registered
        if RydeUser.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already registered'}, status=400)

        # Create a new LimoUser instance and save it to the database
        ryde_user = RydeUser(
            name=name,
            email=email,
            phone_number=phone_number,
            password=password,
        )
        ryde_user.save()

        return JsonResponse({'message': 'rydeUser signup successful'}, status=200)


class LoginRydeUserView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return JsonResponse({'error': 'All fields are required'}, status=400)
        try:
            user = LimoUser.objects.get(email=email)
            if user.password != password:
                return JsonResponse({'error': 'Incorrect password'}, status=400)

            token, created = CustomUserToken.objects.get_or_create(user=user)
            return JsonResponse({'token': token.key, 'email': email}, status=200)

        except ObjectDoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)