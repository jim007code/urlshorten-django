import random
import string

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, auth
from django.http import JsonResponse
from django.shortcuts import render

from .models import *

# Create your views here.
def register(request):
    if request.method == 'POST':
        # Handle user registration form data
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Hash the password before storing
        hashed_password = make_password(password)
        
        user = UserProfile(username=username, password=hashed_password)
        user.save()
        return JsonResponse({'message': 'User registered successfully'})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            token = generate_jwt_token(user)
            return JsonResponse({'token': token})
        else:
            return JsonResponse({'message': 'Login failed'}, status=401)

def user_logout(request):
    logout(request)
    return JsonResponse({'message': 'Logged out'})

# //////////////////


@login_required
def shorten_url(request):
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        user = request.user

        # Generate a random short code
        short_code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

        # Save the shortened URL
        shortened_url = ShortenedURL(original_url=original_url, short_code=short_code, user=user)
        shortened_url.save()

        return JsonResponse({'short_url': f'http://yourdomain.com/{short_code}'})

@login_required
def get_shortened_urls(request):
    user = request.user
    shortened_urls = ShortenedURL.objects.filter(user=user)
    # Return a list of user's shortened URLs
    urls = [{'original_url': url.original_url, 'short_url': f'http://yourdomain.com/{url.short_code}'} for url in shortened_urls]
    return JsonResponse(urls, safe=False)
