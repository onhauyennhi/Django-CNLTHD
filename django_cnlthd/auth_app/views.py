from cmath import log
from tkinter import E
from django.shortcuts import redirect, render
from django.contrib import messages
from auth_app.models import User
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect,HttpResponse
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.get(username = email)

        if not user_obj:
            messages.warning(request, 'Account not found.')
            return HttpResponseRedirect(request.path_info)

        user_obj = authenticate(username = email , password= password)
        if user_obj:
            login(request , user_obj)
            return redirect('/')

        messages.warning(request, 'Invalid credentials')
        return HttpResponseRedirect(request.path_info)


    return render(request ,'auth_app/login.html')

@csrf_protect
def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get("username")
        password = request.POST.get('password')
        try:
            user_exist = User.objects.get(username=username)
            if user_exist:
                messages.warning(request, 'Username is already taken.')
                return HttpResponseRedirect(request.path_info)
        except User.DoesNotExist:
            pass
    
        try:
            user_exist = User.objects.get(email=email)
            if user_exist:
                messages.warning(request, 'Email is already taken.')
                return HttpResponseRedirect(request.path_info)
        except User.DoesNotExist:
            pass
        user_obj = User.objects.create(first_name = first_name , last_name= last_name , email = email , username = email)
        user_obj.set_password(password)
        user_obj.save()

        return HttpResponseRedirect(request.path_info)
    return render(request ,'auth_app/register.html')


def sign_out(request):
    logout(request)
    return redirect('index')















# from django.shortcuts import render
# from django.http import JsonResponse
# from rest_framework.views import APIView
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import status
# from auth_app.models import User

# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         if not username or not password:
#             return JsonResponse(
#                 status=status.HTTP_400_BAD_REQUEST,
#                 data={
#                     "detail": "Please provide credentials to login!"
#                 }
#             )           

#         user = authenticate(
#             username=username, password=password)
        
#         if not user:
#             return JsonResponse(
#                 status=status.HTTP_400_BAD_REQUEST,
#                 data={
#                     "detail": "Invalid credentials!"
#                 }
#             )   
        
#         refresh = RefreshToken.for_user(user)

#         return JsonResponse(
#             {
#                'refresh':str(refresh),
#                'access':str(refresh.access_token) 
#             }
#         )
    
# class RegisterView(APIView):
#     template_name = 'auth_app/register.html'

#     def post(self, request):
#         first_name = request.data.get("first_name")
#         last_name = request.data.get("last_name")
#         username = request.data.get("username")
#         email = request.data.get("email")
#         password = request.data.get("password")

#         if not request.data:
#             return JsonResponse(
#                 status=status.HTTP_400_BAD_REQUEST,
#                 data={
#                     "detail": "Please provide information to register account!"
#                 }
#             ) 
#         try:
#             user_exist = User.objects.get(username=username)
#             if user_exist:
#                 return JsonResponse(
#                     status=status.HTTP_400_BAD_REQUEST,
#                     data={
#                         "detail": "Username already exist!"
#                     }
#                 ) 
#         except User.DoesNotExist:
#             pass
    
#         try:
#             user_exist = User.objects.get(email=email)
#             if user_exist:
#                 return JsonResponse(
#                     status=status.HTTP_400_BAD_REQUEST,
#                     data={
#                         "detail": "Email already exist!"
#                     }
#                 ) 
#         except User.DoesNotExist:
#             pass

#         user = User(
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             username=username
#         )
#         user.set_password(password)
#         user.save()

#         # return JsonResponse(
#         #     status=status.HTTP_200_OK,
#         #     data={
#         #         "detail": "Create account successfully!"
#         #     }
#         # ) 
#         return render(request, self.template_name, {"detail": "Account created successfully!"})

#     def get(self, request):
#         return render(request, self.template_name)

# class RestrictedView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         # Your code here
#         return JsonResponse({"response":"YOU ARE ALLOWED HERE"})
