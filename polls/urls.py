from django.urls import path

from . import views

urlpatterns = [
    path('bmi/', views.bmi_intro, name = 'bmi_intro'),
    path('search/', views.search_profiles, name = 'search_profiles'),
    path('home/', views.home, name = 'home'),
    path('newprofile/', views.newprofile, name = 'newprofile'),
    path('display/', views.display, name ='display'),
]
