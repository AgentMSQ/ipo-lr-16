from django.urls import path
from . import views

app_name = 'yoga'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('aboutauthor/', views.about_author, name = 'about_author'),
    path('aboutshop/', views.about_shop, name = 'about_shop')
]