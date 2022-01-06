from django.contrib import admin
from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from thehood import views
urlpatterns=[
    path('', views.home, name = 'home'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'registration/logout.html')),
    path('profile/', views.profile, name='profile'),
    path('hood/', views.hoods, name='hood'),
    path('single_hood/<hood_id>', views.single_hood, name='single-hood'),
    path('new-hood/', views.new_hood, name='new-hood'),
]