from  django.db import  migrations
from django.urls import path
from . import views

urlpatterns=[
    path('',views.post_list,name='post'),
]