from django.urls import path
from . import views
urlpatterns = [
    path('aboutme/',views.aboutme,name='aboutme'),
    path('services/',views.services,name='services'),
    path('contactme/',views.contactme,name='contactMe'),
    
    path('projects/',views.projects,name='projects'),
    path('downloadcv/',views.uploadcv,name='downloadcv'),
]