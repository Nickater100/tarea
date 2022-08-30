from django.db import models

# Create your models here.



class Genres(models.Model):
    name=models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        ordering=["name"]

class Platform(models.Model):
    name= models.CharField(max_length=30)
    manufactured = models.CharField(max_length=50)
    class Meta:
        ordering=('name',)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)

class Publisher(models.Model):
    trade_name= models.CharField(max_length=30)
    founded = models.PositiveIntegerField(default=1997)
    class Meta:
        ordering=('trade_name',)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)

class Videogames(models.Model):
    name= models.CharField(max_length=100, default="HogwartsLegacy")
    published_year= models.PositiveIntegerField(default=1997)
    genres = models.ManyToManyField(Genres)
    platform = models.ManyToManyField(Platform)
    publisher = models.OneToOneField(Publisher, on_delete= models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['name', 'published_year']

    

