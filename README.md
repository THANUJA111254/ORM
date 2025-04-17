# Ex02 Django ORM Web Application
## Date: 17.04.2025

## AIM
To develop a Django application to store and retrieve data from Movies Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![alt text](<Screenshot 2025-04-17 190325.png>)



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM:
```
admin.py


from django.contrib import admin
from .models import Movies,MoviesAdmin
admin.site.register(Movies,MoviesAdmin)

models.py


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
```



## OUTPUT

![alt text](<Screenshot 2025-04-17 142544.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
