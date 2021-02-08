from django.urls import path
from . import views 

urlpatterns = [
    path('helloword/', views.helloword),
    #Criando uma URL, depois disso você deve criar o metodo na view
    path('',views.tasklist,name='task-list'),
    #Aqui a url vai receber um argumento 
    #ex: http://127.0.0.1:8000/yourname/joselito
    path('yourname/<str:name>',views.yourName,name='your-name'),
]