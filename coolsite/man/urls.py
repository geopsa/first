from django.urls import path, include
from .views import *

urlpatterns = [
    #path('', index),
    path('sait/', sait),
    path('main/', main),
    path('about/', about, name='about'),
]