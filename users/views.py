from urllib import response
from django import http
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

# Create your views here.
class RegisterView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'users/register.html'
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"serializer":serializer})
        serializer.save()
        return redirect('login')
    
class ProfileList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'users/profile_list.html'
    
    def get(self, request):
        queryset = User.objects.all()
        return Response({'profiles':queryset})
class LoginUser(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'users/login.html'
    def get(request):
        serializer = UserSerializer()
        
    
class LoginView(APIView):
       
    
    def post(self, request):
        
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('incorrect password')
        
        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            "jwt": token
        }
        
        return redirect ('homepage')
    
    
class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('unauthenticated')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=('HS256'))
            
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        
        
        return Response(serializer.data)
    
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            "message":"logged out"
        }
        return response
    
    # the functions upwards are API based for logging in, signing up and logging out
    
    # The codes below are django based logging system
    
def register(request):
    pass


def profile(request):
    pass

def edit_account(request):
    pass