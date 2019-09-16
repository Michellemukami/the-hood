from django.contrib import admin
from .models import NeighbourHood, UserProfile, Business, Location, Post

admin.site.register(NeighbourHood)
admin.site.register(UserProfile)
admin.site.register(Business)
admin.site.register(Location)
admin.site.register(Post)
