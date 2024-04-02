from django.urls import path 
from  app2.views import *
app_name='xyz'
urlpatterns=[path('app2html/',app2html,name='app2html'),]