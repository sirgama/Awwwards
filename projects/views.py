from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import NewSiteForm
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

@login_required
def NewSite(request):
    user = request.user.id
    tags_objs = []
    
    if request.method == 'POST':
        form = NewSiteForm(request.POST, request.FILES)
        if form.is_valid():
            sitename = form.cleaned_data.get('sitename')
            url = form.cleaned_data.get('url')
            description = form.cleaned_data.get('description')
            category = form.cleaned_data.get('category')
            country = form.cleaned_data.get('country')
            technolog = form.cleaned_data.get('technologies')
            image = form.cleaned_data.get('image')
            tags_list = list(technolog.split(','))
            
            for tag in tags_list:
                t, created = Technologies.objects.get_or_create(title=tag)
                tags_objs.append(t)
            p, created = Site.objects.get_or_create(sitename=sitename, livelink=url, description=description, category=category, country=country, image=image, user_id=user)
            p.technologies.set(tags_objs)
            p.save()
            return redirect('homepage')
    else:
        form = NewSiteForm()
    context = {
        'form':form
    }
    return render(request, 'projects/new_project.html', context)


@login_required
def View_site(request, pk):
    post = Site.objects.get(id=pk)
    
    try:
        ratings = Rating.get_ratings(pk)
        
    except:
        ratings = None
    
    context = {
        'post':post,
        'ratings':ratings
    }
    return render(request, 'projects/singlesite.html', context)