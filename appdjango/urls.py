from django.urls import path
from . import views

app_name = 'appdjango'

urlpatterns = [
    path('', views.home, name='home'),
    path('pagina2/', views.pagina2, name='pagina2'),  
]