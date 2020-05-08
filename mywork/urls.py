from django.urls import path

from . import views
urlpatterns = [
    path ('', views.work, name='work'),
    path('home',views.home,name='home')
]