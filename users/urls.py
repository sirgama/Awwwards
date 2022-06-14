from django.urls import path
from .views import LogoutView, ProfileList, RegisterView, LoginView, SitesList, UserView

urlpatterns = [
   
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view(), name='api-log'),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('profiles', ProfileList.as_view()),
    path('sites', SitesList.as_view()),
    
]