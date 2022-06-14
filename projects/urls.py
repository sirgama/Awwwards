from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='homepage' ),
    path('endpoints/api', views.apipage, name='api-details' ),
    path('sites/new/', views.NewSite, name='new-site'),
    path('rate/', views.rate_site, name='rate-site'),
    path('rateusability/', views.rate_usability, name='rate-usability'),
    path('ratecontent/', views.rate_content, name='rate-content'),
    path('sites/<int:pk>', views.View_site, name='view-site'),
    path('search/', views.search_results, name='search_results'),
]
