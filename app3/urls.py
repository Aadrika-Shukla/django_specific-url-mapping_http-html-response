from django.urls import path 
from  app3.views import *
app_name='abc'
urlpatterns=[
    path('app3html/',app3html,name='app3html'),
    ]