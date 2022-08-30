from django.contrib import admin
from .models import Genres
from .models import Platform
from .models import Publisher
from .models import Videogames

# Register your models here.

admin.site.register(Genres)
admin.site.register(Platform)
admin.site.register(Publisher)
admin.site.register(Videogames)
