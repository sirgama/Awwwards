from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import NewSiteForm
from .models import RatingContent, RatingUsability, Site, Technologies, Rating
import datetime as dt
from users.models import Profile
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    user = request.user
    site_items = Site.objects.all()
    all_users = User.objects.all()
    date = dt.date.today()
    context = {
        "sites":site_items,
        "users": all_users,
        "current_user": user,
        "date":date,
    }
    return render(request, 'projects/home.html', context)
def search_results(request):
    
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Site.search_by_sitename(search_term)
        message = f"{search_term}"

        return render(request, 'projects/search.html',{"message":message,"sites": searched_projects})

    else:
        message = "You haven't searched for any projects"
        return render(request, 'projects/search.html',{"message":message})

def apipage(request):
    
    
   
    return render(request, 'projects/api.html')

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

def rate_site(request):
    user = request.user
    if request.method == 'POST':
        
        el_id = request.POST.get('el_id')
        val = request.POST.get('val')
        site = Site.objects.get(id=el_id)
        user_profile = User.objects.get(username=user.username)
        Rating.objects.create(design=val, site=site, author=user_profile)
        
        return JsonResponse({'success':'true', 'score':val}, safe=False)
    return JsonResponse({'success', 'false'})

@csrf_exempt
def rate_usability(request):
    user = request.user
    if request.method == 'POST':
        
        el_id = request.POST.get('el_id')
        val = request.POST.get('val')
        site = Site.objects.get(id=el_id)
        user_profile = User.objects.get(username=user.username)
        RatingUsability.objects.create(usability=val, site=site, author=user_profile)
        
        return JsonResponse({'success':'true', 'score':val}, safe=False)
    return JsonResponse({'success', 'false'})

@csrf_exempt
def rate_content(request):
    user = request.user
    if request.method == 'POST':
        
        el_id = request.POST.get('el_id')
        val = request.POST.get('val')
        site = Site.objects.get(id=el_id)
        user_profile = User.objects.get(username=user.username)
        RatingContent.objects.create(content=val, site=site, author=user_profile)
        
        return JsonResponse({'success':'true', 'score':val}, safe=False)
    return JsonResponse({'success', 'false'})