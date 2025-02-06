from django.urls import path
from . import views

urlpatterns = [
    path('', views.myapp, name='myapp'),
    path('pokedex/api/', views.getData, name='get_data'),
]
