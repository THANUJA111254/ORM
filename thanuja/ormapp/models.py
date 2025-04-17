
from django.db import models
from django.contrib import admin
class Movies(models.Model):
    Movie_id=models.IntegerField(primary_key=True)
    Title=models.CharField(max_length=30)
    Rating=models.IntegerField()
    Language=models.CharField()
    Genre=models.CharField(max_length=20)
    noofseats=models.IntegerField()
    date=models.DateField()

class MoviesAdmin(admin.ModelAdmin):
    list_display=('Movie_id','Title','Rating','Language','Genre','noofseats','date')