from django.contrib import admin
from . models import Bio, Photo
# Register your models here.
admin.site.register([Photo, Bio])

