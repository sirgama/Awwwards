from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Site, Technologies, Rating

from users.models import Profile

# Create your views here.

def home(request):
    user = request.user
    site_items = Site.objects.all()
    all_users = User.objects.all()
    
    context = {
        "sites":site_items,
        "users": all_users,
        "current_user": user,
    }
    return render(request, 'projects/home.html', context)