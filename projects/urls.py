from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='homepage' ),
    path('sites/new/', views.NewSite, name='new-site'),
]
