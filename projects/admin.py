from django.contrib import admin
from .models import RatingContent, RatingUsability, Technologies, Site, Rating
# Register your models here.

admin.site.register(Technologies)
admin.site.register(Site)
admin.site.register(Rating)
admin.site.register(RatingUsability)
admin.site.register(RatingContent)