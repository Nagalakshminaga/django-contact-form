from django.urls import path
from .views import home

#app name to reverse url
app_name='home'

urlpatterns = [
    path('', home, name='home'),
]