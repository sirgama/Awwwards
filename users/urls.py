from django.urls import path
from .views import LogoutView, ProfileList, RegisterView, LoginView, UserView

urlpatterns = [
   
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('profiles', ProfileList.as_view()),
    
]