from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='homepage' ),
    path('sites/new/', views.NewSite, name='new-site'),
    path('rate/', views.rate_site, name='rate-site'),
    path('sites/<int:pk>', views.View_site, name='view-site'),
]
