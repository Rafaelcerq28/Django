from django.contrib import admin

#Importando um model no admin
from .models import Task

admin.site.register(Task)
